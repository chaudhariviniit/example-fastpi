"""Update created_at column

Revision ID: 00fc74231c70
Revises: 7b124a4bbb79
Create Date: 2026-03-16 12:35:39.679379

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '00fc74231c70'
down_revision: Union[str, Sequence[str], None] = '7b124a4bbb79'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "users",
        "created_at",
        existing_type=sa.DateTime(),  # or sa.TIMESTAMP(timezone=True) if already set
        type_=sa.TIMESTAMP(timezone=True),
        nullable=False,
        server_default=sa.text("NOW()")
    )


    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "users",
        "created_at",
        existing_type=sa.TIMESTAMP(timezone=True),
        type_=sa.DateTime(),
        nullable=True,
        server_default=None)

    pass
