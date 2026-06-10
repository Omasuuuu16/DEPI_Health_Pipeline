import pandas as pd
import urllib
from sqlalchemy import create_engine

df = pd.read_csv("student_health_clean.csv")
df["Date_of_birth"] = pd.to_datetime(df["Date_of_birth"], errors="coerce").dt.date
df = df.drop(columns=["Age"], errors="ignore")

# ── Connection ───────────────────────────────────────────────
SERVER = "DESKTOP-F1R3U39"

params = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={SERVER};"
    f"DATABASE=DEPI_Health;"
    f"Trusted_Connection=yes;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# ── Test connection first ─────────────────────────────────────
try:
    with engine.connect() as conn:
        print("Connection successful!")
except Exception as e:
    print("Connection failed:", e)
    exit()

# ── Load ─────────────────────────────────────────────────────
df.to_sql(
    name="student_health",
    schema="Raw",
    con=engine,
    if_exists="append",
    index=False
)

print(f"Done — {len(df)} rows loaded into Raw.student_health")