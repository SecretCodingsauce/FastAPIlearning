"""adding users table

Revision ID: d5b8dc6ee8a3
Revises: e8c3d8ae3605
Create Date: 2026-08-23 19:36:47.279438

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5b8dc6ee8a3'
down_revision: Union[str, Sequence[str], None] = 'e8c3d8ae3605'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
    server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'))


def downgrade() -> None:
    op.drop_table('users')
    pass
