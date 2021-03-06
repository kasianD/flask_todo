"""Fix is_accomplished 5

Revision ID: e59393715f23
Revises: e6f324f3acc6
Create Date: 2020-06-10 21:47:03.016365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e59393715f23'
down_revision = 'e6f324f3acc6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('is_accomplished', sa.Boolean(), server_default=sa.text('false'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'is_accomplished')
    # ### end Alembic commands ###
