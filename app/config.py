class GeonamesConfig:
    POSTAL_CSV_ABS_PATH = 'postal.txt'
    GAZETTEER_CSV_ABS_PATH = 'gazetteer.txt'
    POSTAL_CSV_DELIMITER = "\t"
    GAZETTEER_CSV_DELIMITER = "\t"

    POSTAL_CSV_COLUMN_NAMES = [
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

    POSTAL_CSV_USE_COLUMNS = [
        "postal_code",
        "city",
        "state",
        "state_abbreviation",
        "county",
        "latitude",
        "longitude"
    ]

    GAZETTEER_CSV_COLUMN_NAMES = [
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

    GAZETTER_CSV_USE_COLUMNS = [
        "geonames_id", 
        "name", 
        "alternate_names",
        "latitude",
        "longitude",
        "population",
        "elevation",
        "timezone"
    ]

    def __init__(self, **kwargs):
        allowedKeys = set(['prefix'])

        # Initialize attributes to false
        self.__dict__.update((key, False) for key in allowedKeys)

        # Set provided values
        self.__dict__.update((key,value) for key, value in kwargs.items() if key in allowedKeys)

