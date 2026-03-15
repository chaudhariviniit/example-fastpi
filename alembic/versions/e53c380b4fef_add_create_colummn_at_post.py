"""add create colummn at post

Revision ID: e53c380b4fef
Revises: 10f9e98ca984
Create Date: 2026-03-14 13:48:17.222335

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e53c380b4fef'
down_revision: Union[str, Sequence[str], None] = '10f9e98ca984'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
    "posts",
    sa.Column(
        "created_at",
        sa.TIMESTAMP(timezone=True),
        nullable=False,
        server_default=sa.text("now()")))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts","created_at")
    pass
