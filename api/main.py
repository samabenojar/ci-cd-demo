from fastapi import FastAPI
from sqlalchemy import text
from api.database import engine

app = FastAPI(title = "dbt Orders API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/orders")
def get_orders():
    query = """
        select *
        from public.fct_orders
        order by order_id
        limit 100
    """

    with engine.connect() as conn:
        rows = conn.execute(text(query))
        results = [dict(row._mapping) for row in rows]

    return results

@app.get("/metrics/revenue")
def revenue():
    query = """
        select round(sum(amount), 2) as total_revenue
        from public.fct_orders
    """

    with engine.connect() as conn:
        row = conn.execute(text(query)).fetchone()

    return dict(row._mapping)
    

