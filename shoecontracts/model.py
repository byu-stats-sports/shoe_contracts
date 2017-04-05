import peewee as orm
from playhouse.db_url import connect
import shoecontracts
from shoecontracts import DATABASE_URL
import logging
from pprint import pformat, pprint

logger = logging.getLogger(__name__)

db = connect(DATABASE_URL)

class Teams(orm.Model):
    team_id = orm.PrimaryKeyField()
    abbreviation = orm.CharField(null=True)
    nickname = orm.CharField(null=True)
    min_year = orm.DateField()
    max_year = orm.DateField()
    city = orm.CharField(null=True)
    arena = orm.CharField(null=True)
    arenacapacity = orm.IntegerField(null=True)
    owner = orm.CharField(null=True)
    generalmanager = orm.CharField(null=True)
    headcoach = orm.CharField(null=True)
    dleagueaffiliation = orm.TextField(null=True)

    class Players(orm.Model):
    player_id = orm.PrimaryKeyField()
    first_name = orm.CharField()
    last_name = orm.CharField()
    birthdate = orm.DateField()
    height = orm.IntegerField(null=True, help_text='height in inches')
    weight = orm.IntegerField(null=True)
    position = orm.CharField(null=True)
    from_year = orm.DateField()
    to_year = orm.DateField()
    lane_agility_time = orm.FloatField(null=True)
    modified_lane_agility_time = orm.FloatField(null=True)
    standing_vertical_leap = orm.FloatField(null=True)
    three_quarter_sprint = orm.FloatField(null=True)
    bench_press = orm.IntegerField(null=True)

class ShoeContracts(orm.Model):
    player = orm.ForeignKeyField(Players, related_name='player_name')
    first_name=orm.CharField()
    last_name=orm.CharField()
    team = orm.ForeignKeyField(Teams,related_name='team_name')
    shoe = orm.CharField()
    season = orm.DateField()
    team = orm.CharField()

    class META
        database = db
        db_table= 'shoe_contracts'
        
def create_tables(tables=[ShoeContracts]):
    db.create_tables(tables, safe=True)
    

@db.atomic()
def add(model, data):
    logger.info('Adding data to the {0} database table...'
                .format(model._meta.db_table))
    logger.debug(pformat(list(data)))
    return model.insert_many(data).execute()


@db.atomic()
def update(model, data):
    logger.info('Updating the {0} database table...'
                .format(model._meta.db_table))
    logger.debug(pformat(list(data)))
    for item in data:
        try:
            orm.InsertQuery(model, field_dict=item).upsert().execute()
        # TODO: fix IntegrityError due to `Cannot delete or update a parent row: a foreign key constraint fails`
        except orm.IntegrityError as e:
            # seems to be the only way to access e.errno
            # TODO: figure out a better way to only print when not a duplicate key
            if e.args[0] != 1062:
                logger.warning('{}: {!r}'.format(item, e))
                # raise e  # TODO: we might want to raise errors that are anything besides duplicate key errors 
