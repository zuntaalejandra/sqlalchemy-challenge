# sqlalchemy-challenge


Welcome to the SQLAlchemy 's analysis based on 2 tables of data (Measurement and Station) from a BD accessed by commands of sqlalchemy library.


# PART 1


This work includes 2 graphs with pandas python library.


After analize data, an histogram was created. Data used: Temperature data for station USC00519281 from the last 12 months.

 <p align="center"><img src="https://github.com/zuntaalejandra/sqlalchemy-challenge/blob/main/Images/Histogram_station.png" /></p>

The next image, shows the precipitation data from the last 12 months.

 <p align="center"><img src="https://github.com/zuntaalejandra/sqlalchemy-challenge/blob/main/Images/precipitation_Graph.png" /></p>

To check the analysis code, review this file:

 *SurfsUp\analysis_SQLAlchemy.ipynb*



# PART 2

You'll see a Flask API based on the queries from the PART 1 developed.
See the routes in the next image:

 <p align="center"><img src="https://github.com/zuntaalejandra/sqlalchemy-challenge/blob/main/Images/api_page.png" /></p>

The first route:  /api/v1.0/precipitation

Functionality 
**** Obtains date and prcp fields of Measurement table, but just the last 12 months of data.

See the API response in the next image:

<p align="center"><img src="https://github.com/zuntaalejandra/sqlalchemy-challenge/blob/main/Images/precipitation_API.png" /></p>

The second route:  /api/v1.0/stations

Functionality 
**** # Returns all stations found in the table.

See the API response in the next image:

<p align="center"><img src="https://github.com/zuntaalejandra/sqlalchemy-challenge/blob/main/Images/stations_API.png" /></p>

The third route:  /api/v1.0/tobs

Functionality 
**** # Returns date and tobs fields of Measurement table, of the most active station, but just the last 12 months of data.

See the API response in the next image:

<p align="center"><img src="https://github.com/zuntaalejandra/sqlalchemy-challenge/blob/main/Images/tobs_API.png" /></p>




