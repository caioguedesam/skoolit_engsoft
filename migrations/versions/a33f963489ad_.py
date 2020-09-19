"""empty message

Revision ID: a33f963489ad
Revises: ac91db362bc8
Create Date: 2020-09-19 15:05:25.240818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a33f963489ad'
down_revision = 'ac91db362bc8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('modulos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('titulo', sa.String(), nullable=False),
    sa.Column('turma_id', sa.Integer(), nullable=False),
    sa.Column('texto', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['turma_id'], ['turmas.id'], name=op.f('fk_modulos_turma_id_turmas')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_modulos'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('modulos')
    # ### end Alembic commands ###