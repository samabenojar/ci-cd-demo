from fastapi import FastAPI

from api.routers.orders import router as orders_router
from api.routers.metrics import router as metrics_router

app = FastAPI(title = "dbt Orders API")


@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(orders_router)
app.include_router(metrics_router)

