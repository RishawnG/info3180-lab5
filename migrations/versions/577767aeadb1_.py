"""empty message

Revision ID: 577767aeadb1
Revises: 7f0567d7a2f9
Create Date: 2019-03-01 19:47:09.538010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '577767aeadb1'
down_revision = '7f0567d7a2f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###
