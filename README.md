# PICKUP_API
## Packages

The API was built with Flask and most of the modules I have used are in-built Python modules. Only one of them require pip installation. And that is: python-dateutil. It can be installed with the following command: 

pip install python-dateutil

I used it for easy and seamless handling of datetime date. All necessary packages are listed in the requirements.txt file. 

## Set Up

The csv files have been placed in the same directory as the application files. I have used the same endpoint that was provided: /median_pickup_time, and it accepts location id, start time and end time parameters as specified. The return value is the median pickup time. 

Sample Request:

HTTP GET
/median_pickup_time?location_id=12&start_time=2019-01-09T11:00:00&end_time=
2019-01-09T12:00:00

Sample Response:
{
    "median": 24
}

I did not use Flask-RESTful or Django REST Framework since models were not involved. 
