from .csv import CsvImportConfig
 
class GeonamesPostalConfig(CsvImportConfig):
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


class GeonamesGazetteerConfig(CsvImportConfig):
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
