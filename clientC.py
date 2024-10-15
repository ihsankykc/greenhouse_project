import requests
import random
import time
from datetime import datetime

delay = 7 

def generate_data(sensor_id):

    light_level = round(random.randint(50000,60000)/100,2)
    temprature = round(random.randint(2100,2200)/100,2)
    humidity = round(random.randint(5800,6000)/100,2)
    rightNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {
        'sensor_id': sensor_id ,
        'time' : rightNow ,
        'light_level' : light_level ,
        'temprature' : temprature ,
        'humidity' : humidity
    }

    return data
   

def send_data(data):
    # Send the generated data to the Flask server
    url = 'http://localhost:5000/receive_data'
    headers = {'Content-Type': 'application/json'}  # Set the request headers
    response = requests.post(url, json=data, headers=headers)  # Send POST request
    
    if response.status_code == 200:
        print("Data sent successfully:", response.json())  # Print server response
    else:
        print("Failed to send data. Status code:", response.status_code)


def send_dataC(data):
    # Send the generated data to the Flask server
    url = 'http://localhost:5000/receive_dataC'
    headers = {'Content-Type': 'application/json'}  # Set the request headers
    response = requests.post(url, json=data, headers=headers)  # Send POST request
    
    if response.status_code == 200:
        print("Data sent successfully:", response.json())  # Print server response
    else:
        print("Failed to send data. Status code:", response.status_code)



if __name__ == '__main__':
    sensor_id = 'C'
    while True:
        data = generate_data(sensor_id)
        send_data(data)
        send_dataC(data)
        time.sleep(delay)  # Wait for 5 seconds before sending the next set of dataS