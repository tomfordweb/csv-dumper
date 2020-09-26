Create a SQLite database of the geonames.org gazetteer and postal code data for any country in the world.

Building:

Set the prefix to whatever 2 character country code you want.

```
$ docker build -t tomfordweb/geonames-us --build-arg PREFIX=US .
$ docker push tomfordweb/geonames-us:latest

```

https://www.geonames.org/
