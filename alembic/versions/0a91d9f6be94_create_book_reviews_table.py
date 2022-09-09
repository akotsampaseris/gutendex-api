"""create book_reviews table

Revision ID: 0a91d9f6be94
Revises: 8c334d3978ec
Create Date: 2022-09-08 16:28:30.153275

"""
from alembic import op
from sqlalchemy import Column, Integer, String, Float


# revision identifiers, used by Alembic.
revision = '0a91d9f6be94'
down_revision = '8c334d3978ec'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "book_reviews",
        Column("id", Integer, primary_key=True),
        Column("book_id", Integer),
        Column("rating", Float, nullable=True),
        Column("review", String, nullable=True)
    )


def downgrade():
        op.drop_table("book_reviews")

