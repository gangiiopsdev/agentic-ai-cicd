from fastapi import FastAPI
import subprocess
from shlex import quote

global_process = None

def create_ping_process(host):
    global global_process
    if global_process and global_process.poll() is not None:
        global_process.terminate()
        global_process.wait()
    command = ['ping', quote(host)]
    # Validate or sanitize the host input before passing to subprocess
    if validate_host(host):
        global_process = subprocess.Popen(command)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    create_ping_process(host)
    return {'status': 'completed'}

# Function to validate or sanitize the host input
def validate_host(host):
    # Implement validation logic here
    allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
    return host in allowed_hosts