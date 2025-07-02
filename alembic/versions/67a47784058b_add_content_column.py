"""add content column

Revision ID: 67a47784058b
Revises: 63e3c03f9fd4
Create Date: 2025-07-02 12:55:00.348517

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67a47784058b'
down_revision: Union[str, Sequence[str], None] = '63e3c03f9fd4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
   
    


def downgrade():
    op.drop_column('posts','content')
  
