"""empty message

Revision ID: 68a61470d616
Revises: 87b9b825daca
Create Date: 2019-02-17 15:12:32.427138

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '68a61470d616'
down_revision = '87b9b825daca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('atributos_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['atributos_id'], ['atributos.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('escolaridade',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('instituicao', sa.String(length=250), nullable=False),
    sa.Column('curso', sa.String(length=150), nullable=False),
    sa.Column('grau', sa.String(length=150), nullable=False),
    sa.Column('status', sa.String(length=150), nullable=False),
    sa.Column('inicio', sa.Date(), nullable=False),
    sa.Column('termino', sa.Date(), nullable=False),
    sa.Column('atributos_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['atributos_id'], ['atributos.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('familiares',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('relacao', sa.String(length=150), nullable=False),
    sa.Column('atributos_id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['atributos_id'], ['atributos.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profissoes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('empresa', sa.String(length=250), nullable=False),
    sa.Column('cargo', sa.String(length=250), nullable=False),
    sa.Column('dataInicio', sa.Date(), nullable=False),
    sa.Column('dataTermino', sa.Date(), nullable=True),
    sa.Column('atributos_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['atributos_id'], ['atributos.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('atributos', sa.Column('usuario_id', sa.Integer(), nullable=True))
    op.drop_constraint('atributos_ibfk_1', 'atributos', type_='foreignkey')
    op.drop_constraint('atributos_ibfk_2', 'atributos', type_='foreignkey')
    op.create_foreign_key(None, 'atributos', 'usuarios', ['usuario_id'], ['id'], ondelete='CASCADE')
    op.drop_column('atributos', 'telefone_id')
    op.drop_column('atributos', 'endereco_id')
    op.add_column('enderecos', sa.Column('atributos_id', sa.Integer(), nullable=False))
    op.add_column('enderecos', sa.Column('bairro', sa.String(length=100), nullable=False))
    op.add_column('enderecos', sa.Column('cep', sa.String(length=30), nullable=False))
    op.add_column('enderecos', sa.Column('cidade', sa.String(length=100), nullable=False))
    op.add_column('enderecos', sa.Column('estado', sa.String(length=100), nullable=False))
    op.create_foreign_key(None, 'enderecos', 'atributos', ['atributos_id'], ['id'], ondelete='CASCADE')
    op.drop_column('enderecos', 'endereco')
    op.drop_column('enderecos', 'logradouro')
    op.add_column('telefones', sa.Column('atributos_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'telefones', 'atributos', ['atributos_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('usuarios_ibfk_1', 'usuarios', type_='foreignkey')
    op.drop_column('usuarios', 'atributos_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuarios', sa.Column('atributos_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.create_foreign_key('usuarios_ibfk_1', 'usuarios', 'atributos', ['atributos_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'telefones', type_='foreignkey')
    op.drop_column('telefones', 'atributos_id')
    op.add_column('enderecos', sa.Column('logradouro', mysql.VARCHAR(length=150), nullable=False))
    op.add_column('enderecos', sa.Column('endereco', mysql.VARCHAR(length=150), nullable=False))
    op.drop_constraint(None, 'enderecos', type_='foreignkey')
    op.drop_column('enderecos', 'estado')
    op.drop_column('enderecos', 'cidade')
    op.drop_column('enderecos', 'cep')
    op.drop_column('enderecos', 'bairro')
    op.drop_column('enderecos', 'atributos_id')
    op.add_column('atributos', sa.Column('endereco_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('atributos', sa.Column('telefone_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'atributos', type_='foreignkey')
    op.create_foreign_key('atributos_ibfk_2', 'atributos', 'telefones', ['telefone_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('atributos_ibfk_1', 'atributos', 'enderecos', ['endereco_id'], ['id'], ondelete='CASCADE')
    op.drop_column('atributos', 'usuario_id')
    op.drop_table('profissoes')
    op.drop_table('familiares')
    op.drop_table('escolaridade')
    op.drop_table('email')
    # ### end Alembic commands ###
