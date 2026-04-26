import os
import psycopg2


DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "analytics")
DB_USER = os.getenv("DB_USER", "sam")
DB_PASSWORD = os.getenv("DB_PASSWORD", "sam_password")
DB_SCHEMA = os.getenv("DB_SCHEMA", "public")

EXPORT_PATH = "exports/fct_orders.csv"


def export_fct_orders():
    os.makedirs("exports", exist_ok=True)

    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )

    query = f"""
        copy (
            select
                order_id,
                customer_id,
                customer_name,
                signup_date,
                order_date,
                amount,
                status
            from {DB_SCHEMA}.fct_orders
            order by order_id
        )
        to stdout
        with csv header
    """

    with conn:
        with conn.cursor() as cur:
            with open(EXPORT_PATH, "w", encoding="utf-8") as f:
                cur.copy_expert(query, f)

    conn.close()

    print(f"Exported fct_orders to {EXPORT_PATH}")


if __name__ == "__main__":
    export_fct_orders()