"""user phone edit

Revision ID: 01ccea2fb6e9
Revises: 10e7eaf5186d
Create Date: 2024-08-24 20:36:43.034030

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '01ccea2fb6e9'
down_revision: Union[str, None] = '10e7eaf5186d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('ALTER TABLE users ALTER COLUMN phone TYPE INTEGER USING phone::integer;')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'phone',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=20),
               existing_nullable=True)
    # ### end Alembic commands ###
