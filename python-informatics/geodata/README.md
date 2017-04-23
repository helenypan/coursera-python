# Google Map Visualisation with Google Geocoding API
## Input Data Source for API Parameters: where.data
This text file stores all the entries for the API to search with.
## Load Data and Save to Database
### Script geoload.py
This python script reads the input lines in where.data and for each line check to see if it is already on the database, and if we don't have the data for the location, call the geocoding API to retrieve the data (JSON format) and store it in the database.
### Script geoload_geocoder.py
This python scripts simply uses the python library geocoder, reads where.data and store the longitude and latitude of the locations to the databse. Simpler than geoload.py, although does the similar job.

## Read from Databse, Export JSON
### Script geodump.py
This script reads the database and writes to the file where.js, using codecs and json python libraries. 
### Script geodump_geocoder.py
Similar with geodump.py, this script uses io library to write to the file where.js.

## Google Map Visualisation
### JSON Data in where.js
The file where.js stores the JSON data, which contains the location and coordinates. 
### Visualisation by where.html
The html file concists of HTML and JavaScript to visualise a Google Mao. It reads the most recent data in where.js to get the data to be visualised.


