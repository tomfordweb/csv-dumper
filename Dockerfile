###
# Create databases off free geonames information
###
FROM python:latest as geonames-builder

RUN pip install pandas SQLAlchemy

WORKDIR /
# Use wget to download files so docker can cache these.
# zip code database
RUN wget -O us-postal.zip http://download.geonames.org/export/zip/US.zip
RUN unzip us-postal.zip
RUN rm readme.txt
RUN mv US.txt us-postal.txt

# # Gazeteer information
# RUN wget -O us-gazetteer.zip http://download.geonames.org/export/dump/US.zip
# RUN unzip us-gazetteer.zip
# RUN rm readme.txt
# RUN mv US.txt us-gazetteer.txt
               
COPY geonames-import.py .
RUN python geonames-import.py
CMD ["echo", "done"]