"""add content column to posts

Revision ID: f175170fbe1e
Revises: b446d715c9bc
Create Date: 2026-03-13 14:39:52.747017

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f175170fbe1e'
down_revision: Union[str, Sequence[str], None] = 'b3b460a31450'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts","content")
    pass
