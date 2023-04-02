"""empty message

Revision ID: 64549c95ea0a
Revises: f952812acfbd
Create Date: 2023-03-14 09:19:16.628028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64549c95ea0a'
down_revision = 'f952812acfbd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=8, asdecimal=2),
               existing_nullable=False)
        batch_op.alter_column('mileage',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=8, asdecimal=2),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.alter_column('mileage',
               existing_type=sa.Float(precision=8, asdecimal=2),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.alter_column('price',
               existing_type=sa.Float(precision=8, asdecimal=2),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###