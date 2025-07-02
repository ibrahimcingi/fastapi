"""a bug fixed about adding new columns

Revision ID: 43054265dc65
Revises: f0a2eee86bb6
Create Date: 2025-07-02 13:38:50.856608

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43054265dc65'
down_revision: Union[str, Sequence[str], None] = 'f0a2eee86bb6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False,server_default='TRUE'))
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')))
   
    
   


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    