"""remove is_done

Revision ID: e33636f96e54
Revises: f4c467b13c23
Create Date: 2020-06-10 21:52:37.991740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e33636f96e54'
down_revision = 'f4c467b13c23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'is_done')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('is_done', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###