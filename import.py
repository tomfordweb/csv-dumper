from pandas import read_csv
from sqlalchemy import create_engine
import click
from app.config.geonames import GeonamesPostalConfig, GeonamesGazetteerConfig
from app.importer.reader import createDataframeFromConfig
from app.config.csv import CsvImportConfig

databaseEngine = create_engine('sqlite:///geonames.sqlite', echo=True)


def configFactory(name:str):
    if name == 'geonames-postal':
        config = GeonamesPostalConfig()
        config.entityName = 'postal'
        config.prefix = 'postal'
        return config

    else:
        raise NameError(f'invalid config "{name}"')



@click.command()
@click.option('--inputfile')
@click.option('--config')
@click.option('--outputstyle')
def importer(inputfile, config, outputstyle):
    # Geonames Postal
    config = configFactory(config)
    config.inputFile = inputfile
    config.outputStyle = outputstyle
    
    df = createDataframeFromConfig(config)

    print(df)
    return
    # Geonames Gazetteer
    # gazetteerConfig = GeonamesGazetteerConfig(prefix=prefix)
    # importGeonamesFromConfig(databaseEngine, gazetteerConfig)


if __name__ == '__main__':
    importer()