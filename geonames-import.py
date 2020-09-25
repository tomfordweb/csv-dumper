import pandas
import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///postal.db', echo=True)
                    
def read_csv(filename, headers, sep="\t"):
    return pandas.read_csv(filename, 
        sep=sep,
        names=headers
    )


if __name__ == '__main__':
    # Geonames Zip database
    us_postal_data_frame = read_csv('us-postal.txt', [
            "countryCode", 
            "postalCode", 
            "placeName", 
            "adminName1", 
            "adminCode1",
            "adminName2",
            "adminCode2",
            "adminName3",
            "adminCode3",
            "latitude",
            "longitude",
            "accuracy"
        ]
    )
    us_postal_data_frame.to_sql('us_postal',  engine)

    # Geonames Gazeteer database
    us_gazetteer_data_frame  = read_csv('us-gazetteer.txt', [
        'geonameid',
        'name',
        'asciiname',
        'alternateNames',
        'convenienceAttribute',
        'latitude',
        'longitude',
        'featureClass',
        'featureCode',
        'countryCode',
        'countryCode2',
        'admin1Code',
        'admin2Code',
        'admin3Code',
        'admin4Code',
        'population',
        'elevation',
        'dem',
        'timezone',
        'modifiedDate'
    ])
    print("be patient..this one takes a while")
    us_gazetteer_data_frame.to_sql('us_gazetteer',  engine)
    print('import success')