# serve.py
from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def handle_request():
    if request.method == 'POST':
        # Handle POST request to stress CPU
        subprocess.Popen(["python3", "stress_cpu.py"])
        return "Stressing CPU initiated!", 200
    elif request.method == 'GET':
        # Handle GET request to get private IP address
        private_ip = socket.gethostbyname(socket.gethostname())
        return f"Private IP Address: {private_ip}", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
