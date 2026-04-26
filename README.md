# README.md

# CI/CD dbt PostgreSQL S3 Pipeline

End-to-end analytics engineering project using:

- dbt
- PostgreSQL
- Docker Compose
- Amazon S3
- GitHub Actions
- FastAPI (next phase)

---

## Project Goal

Build a production-style data pipeline that transforms raw transactional data into analytics-ready models, exports artifacts, stores them in cloud object storage, and later serves them through APIs.

---

## Tech Stack

- Python 3.11
- dbt Core
- PostgreSQL 16
- Docker Compose
- AWS CLI
- Amazon S3
- GitHub Actions
- FastAPI (upcoming)

---

## Architecture

```text
Seed CSV files
    ↓
PostgreSQL raw tables
    ↓
dbt staging models
    ↓
dbt mart models
    ↓
CSV export script
    ↓
Amazon S3
    ↓
FastAPI (next)
````

---

## Current Features

### Data Warehouse

* PostgreSQL running in Docker
* Database: `analytics`

### dbt Models

#### Staging

* `stg_customers`
* `stg_orders`

#### Mart

* `fct_orders`

### Data Quality Tests

Includes:

* `not_null`
* `unique`

### Export Pipeline

Exports:

```text
exports/fct_orders.csv
```

### Cloud Storage

Uploads artifact to:

```text
s3://dbt-s3-fastapi-sam/exports/fct_orders.csv
```

### CI/CD

GitHub Actions runs:

```text
dbt debug
dbt seed
dbt run
dbt test
```

---

## Project Structure

```text
ci-cd-dbt-s3/
│── dbt_project/
│   ├── models/
│   │   ├── staging/
│   │   └── marts/
│   ├── seeds/
│   └── dbt_project.yml
│
│── scripts/
│   ├── export_fct_orders.py
│   └── upload_to_s3.sh
│
│── exports/
│── .github/workflows/
│── docker-compose.yml
│── README.md
```

---

## Local Setup

### Start PostgreSQL

```bash
docker compose up -d
```

### Run dbt

```bash
cd dbt_project
dbt seed
dbt run
dbt test
```

### Export Data

```bash
python ../scripts/export_fct_orders.py
```

### Upload to S3

```bash
../scripts/upload_to_s3.sh dbt-s3-fastapi-sam
```

---

## Example SQL Model

```sql
select
    o.order_id,
    o.customer_id,
    c.customer_name,
    o.order_date,
    o.amount,
    o.status
from {{ ref('stg_orders') }} o
left join {{ ref('stg_customers') }} c
    on o.customer_id = c.customer_id
```

---

## CI/CD Workflow

Located in:

```text
.github/workflows/dbt-ci.yml
```

Triggered on:

* push to `main`
* pull requests

---

## Upcoming Phase

### FastAPI Layer

Planned endpoints:

```text
GET /health
GET /orders
GET /orders/{id}
GET /metrics/revenue
```

---

## Why This Project Matters

Demonstrates practical skills in:

* Analytics Engineering
* Data Modeling
* Data Quality Testing
* Cloud Storage Pipelines
* CI/CD Automation
* Backend API Integration

---

## Author

Sam Abenojar


