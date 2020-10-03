# Create databases off free geonames information
# We need the full python library for pandas
# TODO: optimize container to use alpine
FROM python:3.8 as builder


RUN pip install \
    pandas \
    SQLAlchemy \
    click

WORKDIR /app
               
COPY . .


ENTRYPOINT ["python", "import.py"]


