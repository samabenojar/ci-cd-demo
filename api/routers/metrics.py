from fastapi import APIRouter
from sqlalchemy import text

from api.database import engine
from api.schemas import RevenueMetric


router = APIRouter(prefix="/metrics", tags = ["metrics"] )

@router.get("/revenue", response_model=RevenueMetric)
def get_revenue():
    query = """
        select 
            round(sum(amount), 2) as total_revenue
        from public.fct_orders
    """

    with engine.connect() as conn:
        row = conn.execute(text(query)).fetchone()
    return dict(row._mapping)