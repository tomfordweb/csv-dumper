class CsvImportConfig:
    OUTPUT_OPTION_SQLITE = 'sqlite'
    OUTPUT_OPTION_POSTGRES = 'psql'

    CSV_DELIMITER = "\t"
    CSV_COLUMNS_NAMES = []
    CSV_USE_COLUMNS = []

    @property
    def tableName(self):
        return "%s" % (
            self.entityName.lower()
        )

    @property
    def csvFile(self):
        return "%s.txt" % self.entityName.lower()
    
    
    """<Config(prefix="us")>"""
    def __init__(self):
        self.prefix = None
        self.entityName = None
        self.inputFile = None
        self.outputStyle = None
