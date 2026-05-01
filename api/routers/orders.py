from fastapi import APIRouter, HTTPException
from sqlalchemy import text

from api.database import engine
from api.schemas import Order

router = APIRouter(prefix = "/orders", tags = ["orders"])

@router.get("", response_model=list[Order])
def get_orders():
    query = """
        select 
            order_id,
            customer_id,
            customer_name,
            signup_date,
            order_date,
            amount, 
            status
        from public.fct_orders
        order by order_id
        limit 100
            """
    
    with engine.connect() as conn:
        rows = conn.execute(text(query))
        return [dict(row._mapping) for row in rows]
    

@router.get("/{order_id}", response_model = Order)
def get_order(order_id: int):
    query = """
        select 
            order_id,
            customer_id,
            customer_name,
            signup_date,
            order_date,
            amount, 
            status
        from public.fct_orders
        where order_id = :order_id
    """

    with engine.connect() as conn: 
        row = conn.execute(text(query), {"order_id": order_id}).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail = "Order not found")
    
    return dict(row._mapping)
