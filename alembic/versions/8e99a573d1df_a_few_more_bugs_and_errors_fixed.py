"""a few more bugs and errors fixed

Revision ID: 8e99a573d1df
Revises: 43054265dc65
Create Date: 2025-07-02 13:44:33.165304

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e99a573d1df'
down_revision: Union[str, Sequence[str], None] = '43054265dc65'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
   pass
   


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
   
