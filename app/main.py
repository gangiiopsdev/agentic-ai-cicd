from fastapi import FastAPI
import subprocess
import re
global_process = None

# Define a regular expression to validate the host input
HOST_INPUT_PATTERN = re.compile(r'^[a-zA-Z0-9.-]+$')

def create_ping_process(host):
    global global_process
    if global_process and global_process.poll() is not None:
        global_process.terminate()
        global_process.wait()
    try:
        # Validate the input using a regex pattern
        if not HOST_INPUT_PATTERN.match(host):
            raise ValueError('Invalid host input')
        global_process = subprocess.Popen(['ping', host], shell=False, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return create_ping_process(host)