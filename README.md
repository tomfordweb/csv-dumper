
A minimal image containing an sqlite database of the free [geonames.org](https://www.geonames.org/) gazetteer and postal code data for any country in the world.

This image contains a single file: `geonames-PREFIX.sqlite` where `PREFIX` is the uppercase two character country code. For example - `geonames-US.sqlite`.


# Usage
In your project, pull the image and then do something with it.

```docker
FROM tomfordweb/geonames-sqlite:us-1.3 as geonames-us
FROM tomfordweb/geonames-sqlite:ca-1.3 as geonames-ca

FROM python:3.7.5-alpine
COPY --from=geonames-us geonames-US.sqlite /database/geonames-us.sqlite
COPY --from=geonames-ca geonames-CA.sqlite /database/geonames-ca.sqlite
```


# New Databases

Tags must follow naming convention `tomfordweb/geonames-sqlite:COUNTRYCODE-VERSION`


```
$ docker build \
    --tag tomfordweb/geonames-sqlite:us-1.0 \
    --build-arg PREFIX=US \
    .

$ docker push tomfordweb/geonames-sqlite:us

```

