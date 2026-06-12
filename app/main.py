from fastapi import FastAPI
import subprocess
def run_ping(host):
    # Using subprocess.run for better security
    subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it's safe for pinging
    if is_safe_host(host):
        run_ping(host)
    else:
        raise ValueError('Unsafe host provided')
    return {'status': 'completed'}

def is_safe_host(host):
    # Implement logic to validate the host
    allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
    return host in allowed_hosts