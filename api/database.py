from sqlalchemy import create_engine

DATABASE_URL = "postgresql://sam:sam_password@localhost:5432/analytics"

engine = create_engine(DATABASE_URL)