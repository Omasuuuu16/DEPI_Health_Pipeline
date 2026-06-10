import pandas as pd

# =========================================
# 1. LOAD CSV
# =========================================

encodings = ["utf-8", "utf-8-sig", "cp1252", "latin1"]
df = None

for enc in encodings:
    try:
        df = pd.read_csv("student_health.csv", encoding=enc)
        print(f"Loaded successfully using {enc}")
        break
    except Exception:
        continue

if df is None:
    raise ValueError("Failed to load CSV")

# =========================================
# 2. SCHEMA VALIDATION
# =========================================

EXPECTED_COLUMNS = [
    "sleep_duration", "heart_rate", "bmi",
    "calorie_expenditure", "step_count",
    "exercise_duration", "water_intake",
    "diet_type", "stress_level", "sleep_quality",
    "physical_activity_level", "smoking_alcohol",
    "gender", "health_condition",
    "National_ID", "First_Name", "Last_Name",
    "Date_of_birth"
]

print("\n=== Schema Check ===")
missing = [c for c in EXPECTED_COLUMNS if c not in df.columns]
extra   = [c for c in df.columns if c not in EXPECTED_COLUMNS]
print("Missing columns:", missing if missing else "None")
print("Extra columns  :", extra   if extra   else "None")

# =========================================
# 3. ROW COUNT
# =========================================

print("\n=== Row Count ===")
print("Rows:", len(df))

# =========================================
# 4. NULL CHECK (RAW — before any cleaning)
# =========================================

print("\n=== Null Check (Raw) ===")
print(df.isnull().sum().sort_values(ascending=False))

# =========================================
# 5. FIX ARABIC DECIMAL SEPARATOR + NUMERIC CLEANING
# =========================================

numeric_columns = [
    "sleep_duration", "heart_rate", "bmi",
    "exercise_duration", "water_intake",
    "calorie_expenditure", "step_count"
]

for col in numeric_columns:
    # Fix Arabic decimal point ٫ → .
    df[col] = df[col].astype(str).str.replace("٫", ".", regex=False)
    df[col] = pd.to_numeric(df[col], errors="coerce")

# =========================================
# 6. FIX CATEGORICAL COLUMNS
# =========================================

categorical_cols = [
    "diet_type", "smoking_alcohol",
    "gender", "health_condition"
]

for col in categorical_cols:
    df[col] = df[col].astype(str).str.strip().str.lower()

# =========================================
# 7. ORDINAL COLUMNS (keep as categorical)
# =========================================

problem_cols = [
    "stress_level", "sleep_quality", "physical_activity_level"
]

for col in problem_cols:
    df[col] = df[col].astype(str).str.strip().str.lower()
    print(f"\n{col} values:")
    print(df[col].value_counts().head(10))

# =========================================
# 8. DATE CONVERSION
# =========================================

df["Date_of_birth"] = pd.to_datetime(
    df["Date_of_birth"], dayfirst=True, errors="coerce"
)

# =========================================
# 9. HANDLE DUPLICATES
# =========================================

print("\n=== Duplicate National IDs ===")
dup_ids = df[df["National_ID"].duplicated(keep=False)]["National_ID"].unique()

if len(dup_ids) > 0:
    print("Duplicate records found:")
    print(df[df["National_ID"].isin(dup_ids)][
        ["National_ID", "First_Name", "Last_Name", "Date_of_birth", "health_condition"]
    ].to_string())
    before = len(df)
    df = df.drop_duplicates(subset="National_ID", keep="first")
    print(f"\nRemoved {before - len(df)} duplicate(s). Rows remaining: {len(df)}")
else:
    print("No duplicates found.")

# =========================================
# 10. NEGATIVE VALUES CHECK
# =========================================

print("\n=== Negative Values Check ===")
for col in numeric_columns:
    print(f"{col}: {(df[col] < 0).sum()}")

# =========================================
# 11. AGE CALCULATION
# =========================================

today = pd.Timestamp.today()
df["Age"] = (today - df["Date_of_birth"]).dt.days / 365.25

print("\n=== Age Stats ===")
print(df["Age"].describe().round(2))

# =========================================
# 12. FINAL SUMMARY
# =========================================

print("\n=== FINAL SUMMARY ===")
print("Rows         :", len(df))
print("Total Nulls  :", df.isna().sum().sum())
print("Duplicate IDs:", df["National_ID"].duplicated().sum())
print("\nDone — dataset is clean and ready for SQL Server.")

# =========================================
# 13. EXPORT CLEAN CSV (for SSIS)
# =========================================

df.to_csv("student_health_clean.csv", index=False)
print("Exported: student_health_clean.csv")