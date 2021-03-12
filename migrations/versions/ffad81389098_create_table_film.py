"""create table film

Revision ID: ffad81389098
Revises: b06a4dd7d9cb
Create Date: 2021-03-12 15:35:56.104733

"""
import uuid

from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = 'ffad81389098'
down_revision = 'b06a4dd7d9cb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'film',
        sa.Column('id', UUID(as_uuid=True), default=uuid.uuid4, nullable=False),
        sa.Column('film_name', sa.String(), nullable=False),
        sa.Column('film_duration', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('film_name', name='film_name_key')
    )


def downgrade():
    op.drop_table('film')
