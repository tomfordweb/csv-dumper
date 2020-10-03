from pandas import read_csv
import click
from app.config.csv import CsvImportConfig
from sqlalchemy import create_engine
from app.factory import ColumnFactory

databaseEngine = create_engine('sqlite://', echo=False)

@click.command()
@click.option('--input', '-f' ,'_input', required=True, type=str)
@click.option('--columns', '-c', required=True, type=str)
@click.option('--table', '-t', required=True, type=str)
@click.option('--delimiter', '-d', default="\t")
def importer(_input, columns, table, delimiter):

    columns = ColumnFactory(columns)
    config = CsvImportConfig()
    config.inputFile = _input
    config.table = table
    config.columns = columns.cols
    config.dTypes = columns.dtypes
    config.delimiter = delimiter

    df =  read_csv(config.inputFile,
        sep="\t",
        names=config.columns,
        dtype=config.dTypes
    )
    
    df.to_sql(
        config.table,
        databaseEngine,
        index=False
    )

    with databaseEngine.connect() as conn:
        for line in conn.connection.iterdump():
            if line.startswith('INSERT'):
                print(line)

if __name__ == '__main__':
    importer()