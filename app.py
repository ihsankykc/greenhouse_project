from flask import Flask, render_template, jsonify
from flask import request, redirect

app = Flask(__name__)
currentData = []  # Stores the received sensor data
currentDataC = []
currentDataB = []
currentDataA = []
data_lenght = 15


         

@app.route('/')
def init():
    return render_template('initial.html')


@app.route('/register' , methods = ['POST'])
def receive_user():
    global user

    user = request.form['username']

    print("Data received:", user)  # See console...
    return redirect('/hello')

    
@app.route('/hello')
def show_and_register():
    
    return render_template('form.html',
                            name = user )

@app.route('/greenhouse_project')
def show_data():
    return render_template('index.html', currentData=currentData)

@app.route('/greenhouse_project_sensorA')
def show_dataA():
    return render_template('index.html', currentData=currentDataA)


@app.route('/greenhouse_project_sensorB')
def show_dataB():
    return render_template('index.html', currentData=currentDataB)

@app.route('/greenhouse_project_sensorC')
def show_dataC():
    return render_template('index.html', currentData=currentDataC)


@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.get_json()  # Get the JSON data from the POST request
    currentData.append(data)   # Append the new data to the currentData list
   
    if len(currentData)>data_lenght:
     currentData.pop(0)
    
    return jsonify({'status': 'success', 'data_received': data})  # Send a response to the client

@app.route('/receive_dataA', methods=['POST'])
def receive_dataA():
    data = request.get_json()  # Get the JSON data from the POST request
    currentDataA.append(data)   # Append the new data to the currentData list
   
    if len(currentDataA)>data_lenght:
     currentDataA.pop(0)
    
    return jsonify({'status': 'success', 'data_received': data})  # Send a response to the client

@app.route('/receive_dataB', methods=['POST'])
def receive_dataB():
    data = request.get_json()  # Get the JSON data from the POST request
    currentDataB.append(data)   # Append the new data to the currentData list
   
    if len(currentDataB)>data_lenght:
     currentDataB.pop(0)
    
    return jsonify({'status': 'success', 'data_received': data})  # Send a response to the client

@app.route('/receive_dataC', methods=['POST'])
def receive_dataC():
    data = request.get_json()  # Get the JSON data from the POST request
    currentDataC.append(data)   # Append the new data to the currentData list
   
    if len(currentDataC)>data_lenght:
     currentDataC.pop(0)
    
    return jsonify({'status': 'success', 'data_received': data})  # Send a response to the client


@app.route('/network')
def show_network():
    return render_template('network.html')


@app.route('/data')
def display_archieve():
    return render_template('data.html')


if __name__ == '__main__':  
    app.run(debug=True)