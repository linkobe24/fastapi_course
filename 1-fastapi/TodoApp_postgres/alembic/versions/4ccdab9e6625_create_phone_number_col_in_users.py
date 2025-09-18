"""create phone_number col in users

Revision ID: 4ccdab9e6625
Revises:
Create Date: 2025-09-17 16:03:00.374318

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4ccdab9e6625"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("users", sa.Column("phone_number", sa.String(), nullable=True))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("users", "phone_number")
    pass
