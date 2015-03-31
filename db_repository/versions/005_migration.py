from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
destination = Table('destination', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('nickname', VARCHAR(length=64)),
    Column('address_line1', VARCHAR(length=480)),
    Column('address_line2', VARCHAR(length=480)),
    Column('address_city', VARCHAR(length=64)),
    Column('address_zip', INTEGER),
    Column('distance', FLOAT),
    Column('time', DATETIME),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['destination'].columns['address_city'].drop()
    pre_meta.tables['destination'].columns['address_line1'].drop()
    pre_meta.tables['destination'].columns['address_line2'].drop()
    pre_meta.tables['destination'].columns['address_zip'].drop()
    pre_meta.tables['destination'].columns['distance'].drop()
    pre_meta.tables['destination'].columns['time'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['destination'].columns['address_city'].create()
    pre_meta.tables['destination'].columns['address_line1'].create()
    pre_meta.tables['destination'].columns['address_line2'].create()
    pre_meta.tables['destination'].columns['address_zip'].create()
    pre_meta.tables['destination'].columns['distance'].create()
    pre_meta.tables['destination'].columns['time'].create()
