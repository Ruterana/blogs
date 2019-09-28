"""Initial Migration

Revision ID: e9d0255d3b99
Revises: bddc934507a8
Create Date: 2019-09-28 16:17:03.740881

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e9d0255d3b99'
down_revision = 'bddc934507a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('written_on', sa.DateTime(), nullable=True))
    op.drop_column('blogs', 'writted')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('writted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('blogs', 'written_on')
    # ### end Alembic commands ###