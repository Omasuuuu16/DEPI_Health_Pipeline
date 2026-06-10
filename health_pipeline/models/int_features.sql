{{ config(materialized='table') }}

SELECT
    *,
    CASE
        WHEN bmi < 18.5                THEN 'Underweight'
        WHEN bmi BETWEEN 18.5 AND 24.9 THEN 'Normal'
        WHEN bmi BETWEEN 25.0 AND 29.9 THEN 'Overweight'
        ELSE                                'Obese'
    END AS bmi_category,
    CASE WHEN sleep_duration >= 7.0 THEN 1 ELSE 0 END AS sleep_adequate,
    CASE WHEN water_intake >= 2.0   THEN 1 ELSE 0 END AS hydration_adequate,
    ROUND((
        (CAST(step_count AS FLOAT) / 14999.0) * 40 +
        (CAST(exercise_duration AS FLOAT) / 120.0) * 35 +
        (CAST(calorie_expenditure AS FLOAT) / 3901.0) * 25
    ), 2) AS activity_score
FROM {{ ref('stg_student_health') }}