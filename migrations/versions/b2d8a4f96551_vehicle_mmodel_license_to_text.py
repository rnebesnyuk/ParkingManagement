"""vehicle mmodel license to text

Revision ID: b2d8a4f96551
Revises: 8a5cb0b9ba04
Create Date: 2024-08-25 15:01:34.364978

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b2d8a4f96551'
down_revision: Union[str, None] = '8a5cb0b9ba04'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vehicles', 'license_plate',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.Text(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vehicles', 'license_plate',
               existing_type=sa.Text(length=20),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)
    # ### end Alembic commands ###
