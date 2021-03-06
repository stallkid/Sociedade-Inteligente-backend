"""empty message

Revision ID: 784e6de21146
Revises: 8dc6b7729d49
Create Date: 2019-02-17 10:57:17.091312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '784e6de21146'
down_revision = '8dc6b7729d49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('atributos', sa.Column('cpf', sa.String(length=30), nullable=False))
    op.add_column('atributos', sa.Column('dataDeNascimento', sa.DateTime(), nullable=False))
    op.add_column('atributos', sa.Column('estadoCivil', sa.String(length=50), nullable=False))
    op.add_column('atributos', sa.Column('idade', sa.Integer(), nullable=False))
    op.add_column('atributos', sa.Column('nome', sa.String(length=250), nullable=False))
    op.add_column('atributos', sa.Column('rg', sa.String(length=30), nullable=False))
    op.add_column('atributos', sa.Column('sexo', sa.String(length=15), nullable=False))
    op.create_unique_constraint(None, 'atributos', ['rg'])
    op.create_unique_constraint(None, 'atributos', ['cpf'])
    op.create_unique_constraint(None, 'atributos', ['nome'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'atributos', type_='unique')
    op.drop_constraint(None, 'atributos', type_='unique')
    op.drop_constraint(None, 'atributos', type_='unique')
    op.drop_column('atributos', 'sexo')
    op.drop_column('atributos', 'rg')
    op.drop_column('atributos', 'nome')
    op.drop_column('atributos', 'idade')
    op.drop_column('atributos', 'estadoCivil')
    op.drop_column('atributos', 'dataDeNascimento')
    op.drop_column('atributos', 'cpf')
    # ### end Alembic commands ###
