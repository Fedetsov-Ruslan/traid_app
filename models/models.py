from datetime import datetime
from sqlalchemy import JSON, Boolean, MetaData, Table, Column, String, Integer, TIMESTAMP, ForeignKey



metadata = MetaData()

role = Table(
    'role',
    metadata,
    Column("id", Integer, primary_key=True),
    Column('name', String(50), nullable=False),
    Column('permishions', JSON),    
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(50), nullable=False),
    Column("username", String(50), nullable=False),
    Column("hashed_password", String(50), nullable=False),
    Column('registrete_at', TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)


