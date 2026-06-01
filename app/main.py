from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    return run_ping(host)
def is_safe_host(host):
    # Implement a function to validate the host input
    allowed_hosts = ['example.com', 'another-example.com']
    return host in allowed_hosts