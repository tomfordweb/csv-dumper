from ..config import GeonamesConfig
from pandas import read_csv


def importGeonamesPostal(databaseEngine, config: GeonamesConfig):
    postal_data_frame = read_csv(config.POSTAL_CSV_ABS_PATH,
        sep=config.POSTAL_CSV_DELIMITER,
        names=config.POSTAL_CSV_COLUMN_NAMES,
        usecols=config.POSTAL_CSV_USE_COLUMNS
    )

    postal_data_frame.to_sql(
        '%s_postal' % config.prefix.lower(),
        databaseEngine
    )

def importGeonamesGazetteer(databaseEngine, config: GeonamesConfig):
    gazetteer_data_frame  = read_csv(config.GAZETTEER_CSV_ABS_PATH,
        sep=config.GAZETTEER_CSV_DELIMITER,
        names=config.GAZETTEER_CSV_COLUMN_NAMES,
        usecols=config.GAZETTER_CSV_USE_COLUMNS
    )

    gazetteer_data_frame.to_sql(
        '%s_gazetteer' % config.prefix.lower(),
        databaseEngine
    )

def importGeonames(databaseEngine, config: GeonamesConfig):
    importGeonamesPostal(databaseEngine, config)
    importGeonamesGazetteer(databaseEngine, config)
    