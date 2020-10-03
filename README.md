Processes a CSV file and outputs SQL insert statments.

# Usage

```
$ docker build -t database-importer tomfordweb/csv-dumper:latest
$ docker run database-importer \
    -f=data.csv  \
    -c=foo:str,bar:int,baz,fizz,buzz  \
    -t=table > /tmp/database-dump.sql

```

# Arguments

## `--input`,`-i`
The input CSV data to process. It is important that this not contain any headers.

## `--columns`, `-c`
The columns of the CSV file, you can also provide data types for the columns if they are known.

Providing datatypes should be done as much as possible and will provide a much better experience when working with large CSV files or ones with lots of bad data.

Each column should be seperated by a comma `,`
Each datatype for the column is seperated by a colon `:`

Example:

```
--columns foo:str,bar:int,baz:float,fizz,buzz
```

The above argument will tell pandas that the column `foo` contains strings, the column `bar` contains integers, the column `baz` contains floats, and `fizz` and `buzz` are unknown.

Pandas will still atttempt to infer the datatype if you do not provide one, however it consumes more memory and time.

You can read more about dtypes [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#basics-dtypes)

## `--table`, `-t`

The SQL table to dump into

## `--delimiter`,`-d`

The delimter of the CSV, defaults to tab
