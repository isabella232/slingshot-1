
# Slingshot Sample Instructions

!["Taxi"](/images/manh_cab.0.0.jpg)

## Description 
NYC Taxi and Limousine Commission (TLC) Trip Record Data is valuable to
understanding traffic patterns across the New York City region.  This data
is availble monthly in CSV form and averages 25 GiB per calendar year.  
Each year is archived and independently uploaded into Filecoin.

Source 

[User Guide](https://www1.nyc.gov/assets/tlc/downloads/pdf/trip_record_user_guide.pdf) 
(also on Filecoin below)


## Data Structure

Each month contains 4 CSV's and uses the following naming convention  (YYYY_MM_type.csv)

Type is indicated in the table below and can be one of four values (yellow, green, forhire, hv_forhire)

| Type | Description | Dictionary |
|------|-------------| ---------- |
| yellow | Yellow Taxi Trip Records |[Yellow Trips Data Dictionary](https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf) |
| green | Green Taxi Trip Records | [Green Trips Data Dictionary](https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_green.pdf) |
| fhv | FHV Trips Data Dictionary | [For-Hire Vehicle Trip Records](https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_fhv.pdf) |
| hvfhv |High Volume For-Hire Vehicle Trip Records | [High Volume FHV Trips Data Dictionary](https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_hvfhs.pdf) |


A particular year is archived and compressed using standard tar and gzip and a tar.gz extension.


## Directory Example (/images/folder.png "Taxi")

When extracted, the directory structure should look like the following:

(e.g. 2019)


```
2019/
	01/
		2019_01_yellow.csv 
		2019_01_green.csv
		2019_01_fhv.csv
		2019_01_hvhfv.csv 
	02/
		2019_02_yellow.csv 
		2019_02_green.csv
		2019_02_fhv.csv
		2019_02_hvhfv.csv 

	03/
	...
	11/
		2019_11_yellow.csv 
		2019_11_green.csv
		2019_11_fhv.csv
		2019_11_hvfhv.csv 

	12/
		2019_12_yellow.csv 
		2019_12_green.csv
		2019_12_fhv.csv
		2019_12_hvfhv.csv 
```

## Datasource Docs

The docs are also stored in Filecoin using the following structure:

```
nyc_docs/
    trip_record_user_guide.pdf
	dictionaries/
		data_dictionary_trip_records_yellow.pdf
		data_dictionary_trip_records_green.pdf
		data_dictionary_trip_records_fhv.pdf
		data_dictionary_trip_records_hvfhs.pdf
	maps/
		taxi+_zone_lookup.csv
		taxi_zones_shapefile.zip
		taxi_zone_map_bronx.jpg
		taxi_zone_map_brooklyn.jpg
		taxi_zone_map_manhattan.jpg
		taxi_zone_map_queens.jpg
		taxi_zone_map_staten_island.jpg
```

# Filecoin Data

| Year | cid | size (bytes) | miners |
| -----|-----|--------------|--------|
| 2020 | baadfdsafsadfsafadsfsda | 24000000 | f01515, f01414, f14145 |
| 2019 | baadfdsafsadfsafadsfsda | 24000000 | f01515, f01414, f14145 |
| 2018 | baadfdsafsadfsafadsfsda | 24000000 | f01515, f01414, f14145 |
| docs | baadfdsafsadfsafadsfsda | 24000000 | f01515, f01414, f14145 |

-----
