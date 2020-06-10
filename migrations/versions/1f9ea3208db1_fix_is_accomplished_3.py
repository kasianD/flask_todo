"""Fix is_accomplished 3

Revision ID: 1f9ea3208db1
Revises: 26cd66a2fe33
Create Date: 2020-06-10 21:45:51.565112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f9ea3208db1'
down_revision = '26cd66a2fe33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('is_accomplished', sa.Boolean(), server_default=sa.text('true'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'is_accomplished')
    # ### end Alembic commands ###
