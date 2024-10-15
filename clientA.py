import requests
import time
from datetime import datetime
import serial

try:
    ser = serial.Serial("COM5", baudrate=9600, timeout=1)
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit(1)


def generate_data(sensor_id):

    recieved_info = " :  :  "
    values=["","",""]

    # Check how many characters are in the serial buffer
    bytes_serial = ser.inWaiting()

    
    # Only read if data is available
    if bytes_serial > 0:
    # Read the byte array, decode it to a string, and remove newline characters
        recieved_info = ser.readline().decode().strip()
        print(f"Received info from serial: {recieved_info}")

        values = recieved_info.split(":")

    if recieved_info:
        light_level, humidity, temprature = values
    
    rightNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    
    data = {
        'sensor_id': sensor_id ,
        'time' : rightNow ,
        'light_level' : light_level,
        'temprature' : temprature,
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


def send_dataA(data):
    # Send the generated data to the Flask server
    url = 'http://localhost:5000/receive_dataA'
    headers = {'Content-Type': 'application/json'}  # Set the request headers
    response = requests.post(url, json=data, headers=headers)  # Send POST request
    
    if response.status_code == 200:
        print("Data sent successfully:", response.json())  # Print server response
    else:
        print("Failed to send data. Status code:", response.status_code)


if __name__ == '__main__':
    sensor_id = 'A'
    while True:
        data = generate_data(sensor_id)
        send_data(data)
        send_dataA(data)
        time.sleep(5)  # Wait for 5 seconds before sending the next set of data