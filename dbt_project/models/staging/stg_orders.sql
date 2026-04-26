select 
    order_id, 
    customer_id,
    cast(order_date as date) as order_date,
    cast(amount as numeric(12,2)) as amount, 
    status
from {{ ref('raw_orders') }}