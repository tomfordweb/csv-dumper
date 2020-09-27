from pandas import read_csv
from sqlalchemy import create_engine
import click
from app.config.geonames import GeonamesPostalConfig, GeonamesGazetteerConfig
from app.importer.geonames import importGeonamesFromConfig

databaseEngine = create_engine('sqlite:///geonames.sqlite', echo=True)

@click.command()
@click.option('--prefix')
def importer(prefix):
    # Geonames Postal
    postalConfig = GeonamesPostalConfig(prefix=prefix)
    importGeonamesFromConfig(databaseEngine, postalConfig)

    # Geonames Gazetteer
    gazetteerConfig = GeonamesGazetteerConfig(prefix=prefix)
    importGeonamesFromConfig(databaseEngine, gazetteerConfig)


if __name__ == '__main__':
    importer()