"""create users table

Revision ID: 8bf3439a018c
Revises: 67a47784058b
Create Date: 2025-07-02 13:01:47.720952

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8bf3439a018c'
down_revision: Union[str, Sequence[str], None] = '67a47784058b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),sa.Column('email',sa.String(),nullable=False,unique=True),sa.Column('password',sa.String(),nullable=False),sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False))
   


def downgrade():
    op.drop_table('users')
   