"""create table user

Revision ID: 9e1aa2e5a4a4
Revises: 
Create Date: 2021-03-12 15:29:03.664160

"""
import uuid

from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '9e1aa2e5a4a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', UUID(as_uuid=True), default=uuid.uuid4, nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('first_name', sa.String(), nullable=True),
        sa.Column('last_name', sa.String(), nullable=True),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('role', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email', name='user_email_key')
    )


def downgrade():
    op.drop_table('user')
