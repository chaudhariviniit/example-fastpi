"""add user table

Revision ID: 84b2d25fbcab
Revises: f175170fbe1e
Create Date: 2026-03-13 15:12:53.702203

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84b2d25fbcab'
down_revision: Union[str, Sequence[str], None] = 'f175170fbe1e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("email", sa.String(), nullable=False, unique=True),
        sa.Column("password", sa.String(), nullable=False),
         sa.Column('created_at', sa.DateTime, server_default=sa.func.now(), nullable=False),
    )

    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass
