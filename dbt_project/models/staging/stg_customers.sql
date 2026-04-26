SELECT
    customer_id,
    customer_name, 
    cast(signup_date as date) as signup_date
FROM {{ ref('raw_customers') }}
