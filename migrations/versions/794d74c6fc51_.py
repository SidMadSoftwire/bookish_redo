"""empty message

Revision ID: 794d74c6fc51
Revises: 7be34e47fcd4
Create Date: 2025-05-06 10:24:17.907046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '794d74c6fc51'
down_revision = '7be34e47fcd4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('author', sa.String(), nullable=True),
    sa.Column('isbn', sa.String(), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###
