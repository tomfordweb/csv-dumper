from pandas import read_csv
from sqlalchemy import create_engine
import click
from app.config import GeonamesPostalConfig, GeonamesGazetteerConfig
from app.importer.geonames import importGeonamesPostal, importGeonamesGazetteer

databaseEngine = create_engine('sqlite:///geonames.sqlite', echo=True)


@click.command()
@click.option('--prefix')
@click.option('--schema')
def importer(prefix, schema):
    # Geonames Postal
    postalConfig = GeonamesPostalConfig(prefix=prefix)
    importGeonamesPostal(databaseEngine, postalConfig)

    # Geonames Gazetteer
    gazetteerConfig = GeonamesGazetteerConfig(prefix=prefix)
    importGeonamesGazetteer(databaseEngine, gazetteerConfig)


if __name__ == '__main__':
    importer()