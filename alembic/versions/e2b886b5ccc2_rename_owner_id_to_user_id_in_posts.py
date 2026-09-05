"""rename owner_id to user_id in posts

Revision ID: e2b886b5ccc2
Revises: 6c7da2657a0b
Create Date: 2026-09-05 21:35:22.743516

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2b886b5ccc2'
down_revision: Union[str, Sequence[str], None] = '6c7da2657a0b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('posts', 'owner_id', new_column_name='user_id')


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('posts', 'user_id', new_column_name='owner_id')
