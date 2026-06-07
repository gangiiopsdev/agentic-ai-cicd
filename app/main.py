from fastapi import FastAPI
import subprocess
cimport = 'ping'

app = FastAPI()

def ping(host: str):
    # Validate the host to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = [cimport, host]
    result = subprocess.run(args, check=True)
    return {'status': result.returncode}

@app.get('/ping')
def ping_route(host: str):  # Renamed function to avoid naming conflict with the ping function
    return ping(host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}