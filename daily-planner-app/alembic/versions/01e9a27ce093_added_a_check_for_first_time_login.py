"""Added a check for first time login

Revision ID: 01e9a27ce093
Revises: c1d4153a5778
Create Date: 2024-04-04 16:28:50.835761

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '01e9a27ce093'
down_revision: Union[str, None] = 'c1d4153a5778'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('first_login_completed', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'first_login_completed')
    # ### end Alembic commands ###
