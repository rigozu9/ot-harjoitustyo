"""Initial database schema

Revision ID: 53a32f5ffcea
Revises: 
Create Date: 2024-03-23 14:43:37.194146

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53a32f5ffcea'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Use the op.create_table() method to create a new table
    op.create_table(
        'users',
        sa.Column('username', sa.String(), nullable=False, primary_key=True),
        sa.Column('password', sa.String(), nullable=False)
    )


def downgrade() -> None:
    # Use the op.drop_table() method to drop the table
    op.drop_table('users')
