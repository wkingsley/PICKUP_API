import os
from flask import Flask, request, jsonify
import statistics
from file_reader import csv_reader

app = Flask(__name__)

@app.route('/median_pickup_time')
def get_pickup_time():
  # Assign variables using values from the GET request
  location_id = request.args['location_id']
  start_time = request.args['start_time']
  end_time = request.args.get('end_time') # Won't throw any error if absent since it won't be used 
  file = 'pickup_times.csv' 
  csv_file = os.path.abspath(file)

  # Function call to process the csv file
  pickup_time_dataset = csv_reader(csv_file, location_id, start_time) 

  if pickup_time_dataset:
    # Convert all values from string to int and calculate the median
    median_value = statistics.median(map(int, pickup_time_dataset))
    return jsonify({'median': median_value}), 200
  return jsonify({'median': None}), 404 # In case the file_reader function returned None



if __name__ == "__main__":
  app.run(debug=True)