class ColumnFactory():
    DELIMITER = ','
    TYPE_SLITTER = ':'

    """ columns=foo:str,bar:int,baz:float"""
    """ The type is optional, you do not have to provide it"""
    def __init__(self, columnsString:str):
        self.cols = self._columnFactory(columnsString)
        self.dtypes = self._dtypeFactory(columnsString)
    

    def __repr__(self):
        return f"<ColumnFactory cols='{tuple(self.cols)}' dtypes={self.dtypes}'>"

    def _columnFactory(self, columnsString):
        columnsList = columnsString.split(self.DELIMITER)

        returnColumns = []

        for col in columnsList:
            if self.TYPE_SLITTER not in col:
                returnColumns.append(col)
            else:
                returnColumns.append(col.split(self.TYPE_SLITTER)[0])
        
        return returnColumns

    def _dtypeFactory(self, columnsString):
        columnsList = columnsString.split(self.DELIMITER)

        returnColumns = {}

        for col in columnsList:
            if self.TYPE_SLITTER in col:
                colSplit = col.split(self.TYPE_SLITTER)
                returnColumns[colSplit[0]] = colSplit[1]
        
        return returnColumns