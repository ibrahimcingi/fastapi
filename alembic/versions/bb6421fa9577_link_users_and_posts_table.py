"""link users and posts table

Revision ID: bb6421fa9577
Revises: 8bf3439a018c
Create Date: 2025-07-02 13:23:07.527093

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb6421fa9577'
down_revision: Union[str, Sequence[str], None] = '8bf3439a018c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
  op.add_column('posts',sa.Column('user_id',sa.Integer(),nullable=False))
  op.create_foreign_key('posts_user_fk',source_table='posts',referent_table='users',local_cols=['user_id'],remote_cols=['id'],ondelete='CASCADE')


def downgrade():
  op.drop_constraint('posts','posts_user_fk')
  op.drop_column('posts','user_id')
    
