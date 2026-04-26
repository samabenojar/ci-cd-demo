select 
    o.order_id,
    o.customer_id,
    c.customer_name,
    c.signup_date,
    o.order_date,
    o.amount,
    o.status
from {{ ref('stg_orders') }} o 
left join {{ ref('stg_customers') }} c
    on o.customer_id = c.customer_id