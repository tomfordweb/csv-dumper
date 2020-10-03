from ..config.csv import CsvImportConfig


def saveDataframeToSqlite(df, engine, config: CsvImportConfig):

    df.to_sql(
        config.tableName,
        engine,
        index=False
    )
