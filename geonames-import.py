from pandas import read_csv
from sqlalchemy import create_engine
import click
from app.config import GeonamesConfig
from app.importer.geonames import importGeonames

engine = create_engine('sqlite:///geonames.sqlite', echo=True)


@click.command()
@click.option('--prefix')
@click.option('--schema')
def importer(prefix, schema):
    geonamesConfig = GeonamesConfig(prefix=prefix)
    importGeonames(engine, geonamesConfig)

# Geonames Zip database


    # Geonames Gazeteer database



if __name__ == '__main__':
    importer()