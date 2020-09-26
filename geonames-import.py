from pandas import read_csv
from sqlalchemy import create_engine
import click

engine = create_engine('sqlite:///geonames.sqlite', echo=True)

@click.command()
@click.option('--prefix')
def main(prefix):
# Geonames Zip database
    us_postal_data_frame = read_csv('postal.txt',
        sep="\t",
        names=[
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
        ],
        usecols=["postal_code","city","state","state_abbreviation","county","latitude","longitude"]
    )
    us_postal_data_frame.to_sql('%s_postal' % prefix.lower(),  engine)

    # Geonames Gazeteer database
    us_gazetteer_data_frame  = read_csv('gazetteer.txt',
        sep="\t",
        names=[
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
        ],
        usecols=["geonames_id", "name", "alternate_names","latitude","longitude", "population","elevation","timezone"]
    )
    us_gazetteer_data_frame.to_sql('%s_gazetteer' % prefix.lower(),  engine)


if __name__ == '__main__':
    main()