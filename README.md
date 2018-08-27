# trip_data_preparation
This repository includes the code used for file handling, formatting, modifying and testing trip data.

Citi Bike has made trip data from its bicycles available from 2013 onward. Few days after end of each month the trip data of all the bicycles rented by Citi Bike in New York and Jersey City are added to their AWS S3 bucket. Data files are separated on a monthly basis and from third quarter of 2015 onwards each location has its own files. Collecting data in this context can be solved by downloading the files. 
Preparing trip data consist of reading raw data files, taking the needed values and modifying them for example separating date and time into two fields. Converting digital representation of some field to alphabetical representation for example 0 to male, 1 to female and 2 for unknown in the gender field. 

Trip Data source:	https://s3.amazonaws.com/tripdata/index.html
