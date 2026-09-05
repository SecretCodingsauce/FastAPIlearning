"""adding published to posts

Revision ID: f0e3205d0292
Revises: e2b886b5ccc2
Create Date: 2026-09-05 21:46:18.730066

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0e3205d0292'
down_revision: Union[str, Sequence[str], None] = 'e2b886b5ccc2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts",sa.Column('published',sa.Boolean(),server_default=sa.true()))


def downgrade() -> None:
    op.drop_column('posts','published')
    pass
