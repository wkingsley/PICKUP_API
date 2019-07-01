import csv
from dateutil.parser import parse # For easy datetime handling
from functools import lru_cache # In-built Python module for caching

@lru_cache(maxsize=100)
def csv_reader(file_name, location_id_, start_time_):
  with open(file_name, 'r') as pickup_times:
    # Create csv reader object
    pickup_times_reader = csv.DictReader(pickup_times)
    pickup_times_list = []
    
    # Loop through the csv reader object
    for row in pickup_times_reader:
      # The location_ids from the GET request and csv file are first cast to int for accurate comparison.
      # Also the hour units of both start_time from the GET request and iso_8601_timestamp from the csv file are obtained for accurate comparison.
      if int(location_id_) == int(row['location_id']) and parse(start_time_).hour == parse(row['iso_8601_timestamp']).hour:
        pickup_times_list.append(row['pickup_time'])
    return pickup_times_list
  return None # In case the file was not opened

