from flask import Flask, jsonify, request
from flask_cors import CORS
from subprocess import Popen, PIPE

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/run_faces', methods=['GET', 'POST'])
def execute_faces():
    p = Popen(['python', 'C:/Users/oumai/Desktop/OpenCV-Python-Series/src/faces.py'], stdout=PIPE, stderr=PIPE)
    output, errors = p.communicate()
    if p.returncode != 0:
        return f'Error occurred: {errors.decode()}'
    else:
        return 'Faces.py executed successfully.'

@app.route('/name', methods=['GET', 'POST'])
def name():
    if request.method == 'POST':
        name = request.args.get('name')
        print("Received name:", name) 
        app.name = name  # store the name in a variable in the app object
        return 'Name received successfully!'
    elif request.method == 'GET':
        print("Sent name:", app.name) 
        return jsonify({'name': app.name})  # send the name back to the React app

if __name__ == '__main__':
    app.run(debug=True)
