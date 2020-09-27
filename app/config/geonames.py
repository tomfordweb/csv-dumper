from .importConfig import ImportConfig

class GeonamesConfig(ImportConfig):
    ENTITY_NAME = None
    CSV_DELIMITER = "\t"
    CSV_COLUMNS_NAMES = None
    CSV_USE_COLUMNS = None

    @property
    def tableName(self):
        return "%s_%s" % (
            self.prefix.lower(),
            self.ENTITY_NAME
        )

    @property
    def csvFile(self):
        return "%s.txt" % self.ENTITY_NAME.lower()
    
 
class GeonamesPostalConfig(GeonamesConfig):
    ENTITY_NAME = 'postal'

    CSV_COLUMN_NAMES = [
        "country_code", 
        "postal_code", 
        "city", 
        "state", 
        "state_abbreviation",
        "county",
        "county_code",
        "admin_name_3",
        "admin_code_3",
        "latitude",
        "longitude",
        "accuracy"
    ]

    CSV_USE_COLUMNS = [
        "postal_code",
        "city",
        "state",
        "state_abbreviation",
        "county",
        "latitude",
        "longitude"
    ]


class GeonamesGazetteerConfig(GeonamesConfig):
    ENTITY_NAME = 'gazetteer'

    CSV_COLUMN_NAMES = [
        'geonames_id',
        'name',
        'ascii_name',
        'alternate_names',
        'latitude',
        'longitude',
        'feature_class',
        'feature_code',
        'country_code',
        'country_code2',
        'admin1_code',
        'admin2_code',
        'admin3_code',
        'admin4_code',
        'population',
        'elevation',
        'dem',
        'timezone',
        'modified_date'
    ]

    CSV_USE_COLUMNS = [
        "geonames_id", 
        "name", 
        "alternate_names",
        "latitude",
        "longitude",
        "population",
        "elevation",
        "timezone"
    ]
