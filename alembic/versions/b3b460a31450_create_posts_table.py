"""create posts table

Revision ID: b3b460a31450
Revises: 
Create Date: 2026-03-13 13:01:28.464670

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b3b460a31450'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('posts',sa.Column('id',sa.INTEGER(),nullable = False,primary_key=True),
                    sa.Column('title',sa.String(),nullable = False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('posts')
    pass
