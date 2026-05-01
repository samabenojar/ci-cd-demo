from datetime import date
from decimal import Decimal
from pydantic import BaseModel, ConfigDict

class Order(BaseModel):
    order_id: int
    customer_id: int
    customer_name: str | None
    signup_date: date | None
    order_date: date 
    amount: Decimal
    status: str

    model_config = ConfigDict(from_attributes=True)

class RevenueMetric(BaseModel):
    total_revenue: Decimal | None