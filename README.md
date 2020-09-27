
A minimal image containing an sqlite database of the free [geonames.org](https://www.geonames.org/) gazetteer and postal code data for any country in the world.

This image contains a single file: `geonames-PREFIX.sqlite` where `PREFIX` is the lowercase two character country code. For example - `geonames-us.sqlite`.

Tags must follow naming convention `tomfordweb/geonames-sqlite:COUNTRY-CODE-VERSION`

```
$ docker build \
    --tag tomfordweb/geonames-sqlite:us-1.0 \
    --build-arg PREFIX=US \
    .

$ docker push tomfordweb/geonames-sqlite:us

```

