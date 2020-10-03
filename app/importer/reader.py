from ..config.csv import CsvImportConfig
from pandas import read_csv


def createDataframeFromConfig(config: CsvImportConfig):
    return read_csv(config.inputFile,
        sep=config.CSV_DELIMITER,
        names=config.CSV_COLUMN_NAMES,
        usecols=config.CSV_USE_COLUMNS
    )
