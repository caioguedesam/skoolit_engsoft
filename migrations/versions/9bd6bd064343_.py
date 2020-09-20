"""empty message

Revision ID: 9bd6bd064343
Revises: a33f963489ad
Create Date: 2020-09-20 07:52:57.042259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bd6bd064343'
down_revision = 'a33f963489ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('postagens', schema=None) as batch_op:
        batch_op.add_column(sa.Column('link', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('postagens', schema=None) as batch_op:
        batch_op.drop_column('link')

    # ### end Alembic commands ###