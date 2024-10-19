from flask import Flask
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "B Kiran"  # Change this as per your requirement
    username = os.getlogin()  # This works on Windows too
    server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Use 'tasklist' command to list running processes on Windows
    tasklist_output = subprocess.getoutput('tasklist')

    # Return the output as HTML
    return f"Name: {name}<br>Username: {username}<br>Server Time (IST): {server_time}<br><pre>{tasklist_output}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
