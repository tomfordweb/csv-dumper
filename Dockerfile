###
# Create databases off free geonames information
# We need the full python library for pandas.
###
FROM python:3.8

ARG PREFIX

RUN pip install pandas \
    SQLAlchemy \
    click

WORKDIR /
# Use wget to download files so docker can cache these.
# zip code database
RUN wget -O postal.zip http://download.geonames.org/export/zip/${PREFIX}.zip
RUN unzip postal.zip
RUN rm readme.txt
RUN mv ${PREFIX}.txt postal.txt

# Gazeteer information
RUN wget -O gazetteer.zip http://download.geonames.org/export/dump/${PREFIX}.zip
RUN unzip gazetteer.zip
RUN rm readme.txt
RUN mv ${PREFIX}.txt gazetteer.txt
               
COPY geonames-import.py .
RUN python geonames-import.py --prefix=${PREFIX}

# Note: There seems to be an issue using CMD and the geonames-import script
CMD ["echo", "done"]