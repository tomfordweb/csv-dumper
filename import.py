from pandas import read_csv
import click
from app.config.geonames import GeonamesPostalConfig, GeonamesGazetteerConfig
from app.importer.reader import createDataframeFromConfig
from app.config.csv import CsvImportConfig
from app.importer.sqlite import saveDataframeToSqlite
from sqlalchemy import create_engine


databaseEngine = create_engine('sqlite://', echo=False)


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

    saveDataframeToSqlite(df, databaseEngine, config)
    

    with databaseEngine.connect() as conn:
        for line in conn.connection.iterdump():
            print(line)


    for row in df.items():
        print(row)

if __name__ == '__main__':
    importer()