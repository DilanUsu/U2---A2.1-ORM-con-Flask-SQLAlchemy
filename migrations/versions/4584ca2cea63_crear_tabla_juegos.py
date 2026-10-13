"""crear tabla juegos

Revision ID: 4584ca2cea63
Revises: 
Create Date: 2026-10-13 16:20:19.472592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4584ca2cea63'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('juegos',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('nombre', sa.String(length=255), nullable=False),
        sa.Column('descripcion', sa.String(length=255), nullable=False),
        sa.Column('precio', sa.Numeric(precision=9, scale=2), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('juegos')