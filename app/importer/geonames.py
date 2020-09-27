from ..config.geonames import GeonamesConfig
from pandas import read_csv


def importGeonamesFromConfig(databaseEngine, config: GeonamesConfig):
    postal_data_frame = read_csv(config.csvFile,
        sep=config.CSV_DELIMITER,
        names=config.CSV_COLUMN_NAMES,
        usecols=config.CSV_USE_COLUMNS
    )

    postal_data_frame.to_sql(
        config.tableName,
        databaseEngine
    )
