"""second Migration

Revision ID: 85800ba2f8f9
Revises: 4489936acc19
Create Date: 2022-05-04 13:49:31.094426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85800ba2f8f9'
down_revision = '4489936acc19'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'pass_secure')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###