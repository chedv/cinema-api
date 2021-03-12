"""create table cinema

Revision ID: b06a4dd7d9cb
Revises: 9e1aa2e5a4a4
Create Date: 2021-03-12 15:35:48.707365

"""
import uuid

from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = 'b06a4dd7d9cb'
down_revision = '9e1aa2e5a4a4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'cinema',
        sa.Column('id', UUID(as_uuid=True), default=uuid.uuid4, nullable=False),
        sa.Column('cinema_name', sa.String(), nullable=False),
        sa.Column('cinema_address', sa.String(), nullable=False),
        sa.Column('city_name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('cinema_name', name='cinema_name_key'),
        sa.UniqueConstraint('cinema_address', name='cinema_address_key')
    )


def downgrade():
    op.drop_table('cinema')
