from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate the host input to ensure it's safe
    if not host.isdigit():
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', '-c', '1', host]  # Use '-c' to limit the number of pings
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)