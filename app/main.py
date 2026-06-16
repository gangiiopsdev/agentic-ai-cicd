from fastapi import FastAPI
import subprocess

def run_ping(host):
    try:
        # Validate the host to ensure it's a valid IP address or hostname
        if not validate_host(host):
            raise ValueError('Invalid host')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return run_ping(host)

def validate_host(host):
    import socket
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False