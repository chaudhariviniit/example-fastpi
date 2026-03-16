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
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
