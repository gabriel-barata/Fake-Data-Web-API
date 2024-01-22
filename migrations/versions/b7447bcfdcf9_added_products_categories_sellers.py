"""added products ; categories ;  sellers

Revision ID: b7447bcfdcf9
Revises: 3a35afb9ae12
Create Date: 2024-01-19 16:11:52.454001

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7447bcfdcf9'
down_revision: Union[str, None] = '3a35afb9ae12'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=55), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sellers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=55), nullable=False),
    sa.Column('postcode', sa.String(length=9), nullable=False),
    sa.Column('country', sa.String(length=60), nullable=False),
    sa.Column('city', sa.String(length=85), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ean', sa.BigInteger(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('name_length', sa.String(length=55), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Float(precision=2), nullable=True),
    sa.Column('length', sa.Float(precision=2), nullable=True),
    sa.Column('height', sa.Float(precision=2), nullable=True),
    sa.Column('width', sa.Float(precision=2), nullable=True),
    sa.Column('price', sa.Float(precision=2), nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['seller_id'], ['sellers.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ean')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_table('sellers')
    op.drop_table('categories')
    # ### end Alembic commands ###
