"""add last few columns to posts table

Revision ID: 10f9e98ca984
Revises: 3ede11a9f9d1
Create Date: 2026-03-14 12:41:16.373958

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '10f9e98ca984'
down_revision: Union[str, Sequence[str], None] = '3ede11a9f9d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts",sa.Column("published",sa.Boolean(),nullable=False
                                    ,server_default=sa.text("True")))
    op.add_column(
    "posts",
    sa.Column(
        "created_at",
        sa.TIMESTAMP(timezone=True),
        nullable=False,
        server_default=sa.text("now()")
    )
)
pass

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts","published")
    op.drop_column("posts","created_at")
    pass
