"""Add user_id to activities

Revision ID: 6c3e9bd78e01
Revises: 3fab862670ae
Create Date: 2024-03-24 20:55:52.178759

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c3e9bd78e01'
down_revision: Union[str, None] = '3fab862670ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('activities', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'activities', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'activities', type_='foreignkey')
    op.drop_column('activities', 'user_id')
    # ### end Alembic commands ###
