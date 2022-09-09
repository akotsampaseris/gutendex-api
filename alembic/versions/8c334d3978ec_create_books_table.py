"""create books table

Revision ID: 8c334d3978ec
Revises: 
Create Date: 2022-09-08 16:23:46.233680

"""
from alembic import op
from sqlalchemy import Column, Integer, String, Float


# revision identifiers, used by Alembic.
revision = '8c334d3978ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "books",
        Column("id", Integer, primary_key=True),
        Column("title", String),
        Column("download_count", Integer),
        Column("rating", Float),
    )


def downgrade():
    op.drop_table("books")
