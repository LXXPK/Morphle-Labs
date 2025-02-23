from flask import Flask
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "B Kiran"  
    username = os.getlogin() 
    server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    top_output = subprocess.getoutput('top -b -n1 | head -15')
    tasklist_output = subprocess.getoutput('tasklist')

   
    return f"Name: {name}<br>Username: {username}<br>Server Time (IST): {server_time}<br><pre>{tasklist_output}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
