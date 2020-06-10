"""Add is_accomplished again 2

Revision ID: 4fb730aebeb8
Revises: e33636f96e54
Create Date: 2020-06-10 21:53:22.349464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fb730aebeb8'
down_revision = 'e33636f96e54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('is_accomplished', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'is_accomplished')
    # ### end Alembic commands ###