"""add content column

Revision ID: e8c3d8ae3605
Revises: a35205ab5ef9
Create Date: 2026-08-23 19:24:04.908670

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8c3d8ae3605'
down_revision: Union[str, Sequence[str], None] = 'a35205ab5ef9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
