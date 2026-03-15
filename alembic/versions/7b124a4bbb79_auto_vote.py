"""auto vote

Revision ID: 7b124a4bbb79
Revises: e53c380b4fef
Create Date: 2026-03-14 14:24:10.788774

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '7b124a4bbb79'
down_revision: Union[str, Sequence[str], None] = 'e53c380b4fef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'votes',
        sa.Column('post_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('post_id', 'user_id')
    )

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('votes')