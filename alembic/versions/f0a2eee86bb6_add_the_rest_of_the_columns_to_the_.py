"""add the rest of the columns to the posts table

Revision ID: f0a2eee86bb6
Revises: bb6421fa9577
Create Date: 2025-07-02 13:29:24.564593

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0a2eee86bb6'
down_revision: Union[str, Sequence[str], None] = 'bb6421fa9577'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
  op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False,server_default='TRUE'))
  op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')))
   


def downgrade():
  op.drop_column('posts','published')
  op.drop_column('posts','created_at')
   