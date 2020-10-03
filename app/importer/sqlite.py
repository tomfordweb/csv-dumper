

def saveDataframeToSqlite(df, config:):
    df.to_sql(
        config.tableName,
        databaseEngine,
        index=False
    )
