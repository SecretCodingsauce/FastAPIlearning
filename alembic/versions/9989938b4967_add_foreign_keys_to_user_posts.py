"""add foreign keys to user posts

Revision ID: 9989938b4967
Revises: d5b8dc6ee8a3
Create Date: 2026-08-23 19:59:16.691844

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9989938b4967'
down_revision: Union[str, Sequence[str], None] = 'd5b8dc6ee8a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op. add_column( 'posts' , sa. Column( 'owner_id' , sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
