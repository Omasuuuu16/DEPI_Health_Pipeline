{{ config(materialized='table') }}

SELECT *
FROM {{ source('Raw', 'student_health') }}