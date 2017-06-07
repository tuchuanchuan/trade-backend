"""init tables

Revision ID: 038e34700aae
Revises: 
Create Date: 2017-05-24 11:42:17.776079

"""

# revision identifiers, used by Alembic.
revision = '038e34700aae'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'track',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False, ),
        sa.Column('name', sa.String(128), nullable=False, server_default='', ),
        sa.Column('version', sa.String(128), nullable=False, server_default='', ),
        sa.Column('composer', sa.String(512), nullable=False, server_default='', ),
        sa.Column('lyricist', sa.String(512), nullable=False, server_default='', ),
        sa.Column('isrc', sa.String(16), nullable=False, server_default='', ),
        sa.Column('album_name', sa.String(64), nullable=False, server_default='', ),
        sa.Column('release_company', sa.String(64), nullable=False, server_default='', ),
        sa.Column('label', sa.String(64), nullable=False, server_default='', ),
        sa.Column('description', sa.Text, ),
        sa.Column('duration', sa.Integer(), nullable=False, server_default='0', ),
        sa.Column('file_path', sa.String(512), nullable=False, server_default='', ),
        sa.Column('listen_url', sa.String(512), nullable=False, server_default='', ),
        sa.Column('wave_pic_url', sa.String(512), nullable=False, server_default='', ),
        sa.Column('price', sa.Integer(), nullable=False, server_default='0', ),
        sa.Column('active', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('copyright_id', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('is_oversea', sa.Integer(), nullable=False, server_default='0'),

        sa.Column('created_datetime', sa.DateTime(), nullable=False, ),
        sa.Column('updated_datetime', sa.DateTime(), nullable=False, ),
    )

    op.create_table(
        'tag',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False, ),
        sa.Column('name', sa.String(16), nullable=False, server_default='', ),
        sa.Column('father_id', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('active', sa.Integer(), nullable=False, server_default='0'),
    )

    op.create_table(
        'track_tag_relationship',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False, ),
        sa.Column('track_id', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('tag_id', sa.Integer(), nullable=False, server_default='0'),
    )

    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False, ),
        sa.Column('username', sa.String(64), nullable=False, server_default=''),
        sa.Column('nick', sa.String(32), nullable=False, server_default=''),
        sa.Column('hashed_password', sa.String(128), nullable=False, server_default=''),
        sa.Column('password_salt', sa.String(64), nullable=False, server_default=''),
        sa.Column('forbidden', sa.SMALLINT(), nullable=False, server_default='0'),
        sa.Column('last_login_ip', sa.String(128), nullable=False, server_default=''),
        sa.Column('last_login_time', sa.Integer(), nullable=False, server_default='0'),
    )

    op.create_table(
        'admin',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False, ),
        sa.Column('username', sa.String(64), nullable=False, server_default=''),
        sa.Column('hashed_password', sa.String(128), nullable=False, server_default=''),
        sa.Column('password_salt', sa.String(64), nullable=False, server_default=''),
        sa.Column('level', sa.Integer(), nullable=False, server_default='0', ),
        sa.Column('forbidden', sa.SMALLINT(), nullable=False, server_default='0'),
        sa.Column('last_login_ip', sa.String(128), nullable=False, server_default=''),
        sa.Column('last_login_time', sa.Integer(), nullable=False, server_default='0'),
    )

    op.create_table(
        'cart',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False, ),
        sa.Column('account_id', sa.Integer(), nullable=False, ),
        sa.Column('track_id', sa.Integer(), nullable=False, ),
        sa.Column('amount', sa.Integer(), nullable=False, server_default='1'),
        sa.Column('unit_price', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('deal_type', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('is_deleted', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('created_datetime', sa.DateTime(), nullable=False, ),
    )

    op.create_table(
        'collection',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False, ),
        sa.Column('account_id', sa.Integer(), nullable=False, ),
        sa.Column('track_id', sa.Integer(), nullable=False, ),
        sa.Column('is_deleted', sa.Integer(), nullable=False, server_default='0', ),
        sa.Column('created_datetime', sa.DateTime(), nullable=False, ),
    )

    op.create_table(
        'order',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False, ),
        sa.Column('account_id', sa.Integer(), nullable=False, ),
        sa.Column('status', sa.Integer(), nullable=False, server_default='0', ),
        sa.Column('remark', sa.String(512), nullable=False, server_default='', ),
        sa.Column('created_datetime', sa.DateTime(), nullable=False, ),
        sa.Column('finished_datetime', sa.DateTime(), ),
    )

    op.create_table(
        'order_detail',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False, ),
        sa.Column('order_id', sa.Integer(), nullable=False, ),
        sa.Column('track_id', sa.Integer(), nullable=False, ),
        sa.Column('amount', sa.Integer(), nullable=False, ),
        sa.Column('unit_price', sa.Integer(), nullable=False, ),
        sa.Column('deal_type', sa.Integer(), nullable=False, ),
    )

    op.create_table(
        'search_history',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False, ),
        sa.Column('account_id', sa.Integer(), nullable=False, ),
        sa.Column('keyword', sa.String(512), nullable=False, server_default='', ),
        sa.Column('chosen_track_id', sa.Integer(), nullable=False, ),
        sa.Column('search_datetime', sa.DateTime(), nullable=False, ),
    )


def downgrade():
    op.drop_table('track')
    op.drop_table('tag')
    op.drop_table('track_tag_relationship')
    op.drop_table('user')
    op.drop_table('admin')
    op.drop_table('cart')
    op.drop_table('collection')
    op.drop_table('order')
    op.drop_table('order_detail')
    op.drop_table('search_history')
