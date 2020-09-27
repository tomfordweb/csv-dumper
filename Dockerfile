# Create databases off free geonames information
# We need the full python library for pandas
# TODO: optimize container to use alpine
FROM python:3.8

ARG PREFIX
ARG SCHEMA=sqlite

RUN pip install \
    pandas \
    SQLAlchemy \
    click

WORKDIR /app
# Use wget to download files so docker can cache these.
# zip code database
RUN wget -O postal.zip http://download.geonames.org/export/zip/${PREFIX}.zip
RUN unzip postal.zip
RUN rm readme.txt
RUN mv ${PREFIX}.txt postal.txt

# Gazeteer information
# Appears to be public landmarks, gov buildings, 
# and other publicly available data
RUN wget -O gazetteer.zip http://download.geonames.org/export/dump/${PREFIX}.zip
RUN unzip gazetteer.zip
RUN rm readme.txt
RUN mv ${PREFIX}.txt gazetteer.txt
               
COPY . .
RUN python geonames-import.py \ 
    --prefix=${PREFIX} \
    --schema=${SCHEMA}

# Note: There seems to be an issue using CMD and
# the geonames-import script
CMD ["echo", "done"]