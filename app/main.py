from fastapi import FastAPI
import subprocess
global_process = None

def create_ping_process(host):
    global global_process
    if global_process and global_process.poll() is not None:
        global_process.terminate()
        global_process.wait()
    try:
        # Validate the input to ensure it does not contain malicious content
        if any(char in host for char in ('&&', '|', ';', '`', '$')):
            raise ValueError('Invalid host input')
        # Use a whitelist of allowed hosts or validate IP addresses
        allowed_hosts = ['127.0.0.1', '8.8.8.8']  # Example list
        if host not in allowed_hosts:
            raise ValueError('Host is not in the allowed list')
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