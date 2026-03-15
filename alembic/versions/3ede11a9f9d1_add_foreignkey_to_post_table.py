"""add foreignkey to post table

Revision ID: 3ede11a9f9d1
Revises: 84b2d25fbcab
Create Date: 2026-03-14 12:19:23.221028

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ede11a9f9d1'
down_revision: Union[str, Sequence[str], None] = '84b2d25fbcab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts",sa.Column("owner_id",sa.Integer(),nullable=False))
    op.create_foreign_key("post_user_fk",source_table="posts",referent_table="users",
                          local_cols=["owner_id"],remote_cols=["id"],ondelete="CASCADE")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("post_user_fk",table_name="post")
    op.drop_column("posts","owner_id")
    pass
