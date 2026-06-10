{{ config(materialized='table') }}

SELECT
    *,
    CASE stress_level
        WHEN 'low'    THEN 1
        WHEN 'medium' THEN 2
        WHEN 'high'   THEN 3
    END AS stress_level_encoded,
    CASE sleep_quality
        WHEN 'poor'    THEN 1
        WHEN 'average' THEN 2
        WHEN 'good'    THEN 3
    END AS sleep_quality_encoded,
    CASE physical_activity_level
        WHEN 'sedentary' THEN 1
        WHEN 'moderate'  THEN 2
        WHEN 'active'    THEN 3
    END AS physical_activity_encoded,
    CASE smoking_alcohol
        WHEN 'no'         THEN 0
        WHEN 'occasional' THEN 1
        WHEN 'yes'        THEN 2
    END AS smoking_alcohol_encoded,
    CASE WHEN diet_type = 'veg'      THEN 1 ELSE 0 END AS diet_veg,
    CASE WHEN diet_type = 'non-veg'  THEN 1 ELSE 0 END AS diet_nonveg,
    CASE WHEN diet_type = 'balanced' THEN 1 ELSE 0 END AS diet_balanced,
    CASE WHEN gender = 'male'   THEN 1 ELSE 0 END AS gender_male,
    CASE WHEN gender = 'female' THEN 1 ELSE 0 END AS gender_female,
    CASE WHEN gender = 'other'  THEN 1 ELSE 0 END AS gender_other,
    CASE WHEN gender = 'male'   THEN 1 ELSE 0 END AS gender_encoded,
    CASE health_condition
        WHEN 'fit'       THEN 0
        WHEN 'at-risk'   THEN 1
        WHEN 'unhealthy' THEN 2
    END AS health_condition_encoded
FROM {{ ref('int_features') }}