"""empty message

Revision ID: 0e196be923d6
Revises: f1869a672be1
Create Date: 2020-09-19 10:14:04.451859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e196be923d6'
down_revision = 'f1869a672be1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('modulos', schema=None) as batch_op:
        batch_op.drop_column('data')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('modulos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('data', sa.DATETIME(), nullable=False))

    # ### end Alembic commands ###
