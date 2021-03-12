"""create table cinema_session

Revision ID: 46776c6ef6e6
Revises: cc35612a34b4
Create Date: 2021-03-12 15:36:40.308475

"""
import uuid

from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '46776c6ef6e6'
down_revision = 'ffad81389098'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'cinema_session',
        sa.Column('id', UUID(as_uuid=True), default=uuid.uuid4, nullable=False),
        sa.Column('session_place', sa.String(), nullable=False),
        sa.Column('session_start', sa.DateTime(), nullable=False),
        sa.Column('session_price', sa.Numeric(precision=5, scale=2), nullable=False),
        sa.Column('cinema_id', UUID(as_uuid=True), nullable=False),
        sa.Column('film_id', UUID(as_uuid=True), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['cinema_id'], ['cinema.id'], name='cinema_id_fkey', ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['film_id'], ['film.id'], name='film_id_fkey', ondelete='CASCADE')
    )


def downgrade():
    op.drop_table('cinema_session')
