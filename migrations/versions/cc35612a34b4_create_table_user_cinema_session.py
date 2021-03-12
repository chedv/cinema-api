"""create table user_cinema_session

Revision ID: cc35612a34b4
Revises: ffad81389098
Create Date: 2021-03-12 15:36:31.188073

"""
import uuid

from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = 'cc35612a34b4'
down_revision = '46776c6ef6e6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user_cinema_session',
        sa.Column('user_id', UUID(as_uuid=True)),
        sa.Column('cinema_session_id', UUID(as_uuid=True)),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'],  name='user_id_fkey', ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['cinema_session_id'], ['cinema_session.id'], name='cinema_session_id_fkey', ondelete='CASCADE'),
    )


def downgrade():
    op.drop_table('user_cinema_session')
