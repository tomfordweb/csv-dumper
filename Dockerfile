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

# NOTE: You sould use wget to retreive the CSVS as docker can cache the download
# Postral csv
RUN wget -O postal.zip http://download.geonames.org/export/zip/${PREFIX}.zip && \
    unzip postal.zip && \ 
    rm readme.txt && \
    mv ${PREFIX}.txt postal.txt

# Gazetteer csv
RUN wget -O gazetteer.zip http://download.geonames.org/export/dump/${PREFIX}.zip && \
    unzip gazetteer.zip && \
    rm readme.txt && \
    mv ${PREFIX}.txt gazetteer.txt
               
COPY . .

RUN python geonames-import.py \ 
    --prefix=${PREFIX} \
    --schema=${SCHEMA}

# Note: There seems to be an issue using CMD and
# the geonames-import script
CMD ["echo", "done"]