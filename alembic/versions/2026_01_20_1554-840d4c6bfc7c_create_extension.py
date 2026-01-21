"""create extension

Revision ID: 840d4c6bfc7c
Revises: 
Create Date: 2026-01-20 15:54:13.683003

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '840d4c6bfc7c'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('CREATE EXTENSION postgis')


def downgrade() -> None:
    op.execute('DROP EXTENSION postgis')
