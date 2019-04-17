"""empty message

Revision ID: 988cee505eeb
Revises: 68a61470d616
Create Date: 2019-03-29 16:21:09.553634

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '988cee505eeb'
down_revision = '68a61470d616'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('permissoes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nivel', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nivel')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('permissoes')
    # ### end Alembic commands ###
