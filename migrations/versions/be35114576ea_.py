"""empty message

Revision ID: be35114576ea
Revises: 
Create Date: 2017-01-07 17:36:17.584052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be35114576ea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('bucketlists',
    sa.Column('bucketlist_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), server_default=sa.text(u'now()'), nullable=True),
    sa.Column('date_modified', sa.DateTime(), server_default=sa.text(u'now()'), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['users.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('bucketlist_id')
    )
    op.create_table('bucketlistsitems',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('bucketlist_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), server_default=sa.text(u'now()'), nullable=True),
    sa.Column('date_modified', sa.DateTime(), server_default=sa.text(u'now()'), nullable=True),
    sa.Column('done', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['bucketlist_id'], ['bucketlists.bucketlist_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('item_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bucketlistsitems')
    op.drop_table('bucketlists')
    op.drop_table('users')
    # ### end Alembic commands ###
