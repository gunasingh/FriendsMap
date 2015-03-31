from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
destination = Table('destination', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=64)),
    Column('address_line1', String(length=480)),
    Column('address_line2', String(length=480)),
    Column('address_city', String(length=64)),
    Column('address_zip', Integer),
    Column('distance', Float),
    Column('time', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['destination'].columns['address_city'].create()
    post_meta.tables['destination'].columns['address_line1'].create()
    post_meta.tables['destination'].columns['address_line2'].create()
    post_meta.tables['destination'].columns['address_zip'].create()
    post_meta.tables['destination'].columns['distance'].create()
    post_meta.tables['destination'].columns['time'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['destination'].columns['address_city'].drop()
    post_meta.tables['destination'].columns['address_line1'].drop()
    post_meta.tables['destination'].columns['address_line2'].drop()
    post_meta.tables['destination'].columns['address_zip'].drop()
    post_meta.tables['destination'].columns['distance'].drop()
    post_meta.tables['destination'].columns['time'].drop()
