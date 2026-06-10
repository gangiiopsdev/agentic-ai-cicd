from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Use a whitelist approach for allowed hosts
    allowed_hosts = ['google.com', 'example.com']  # Example list
    if host in allowed_hosts:
        sanitized_host = quote(host)  # Using shlex.quote to safely handle input
        try:
            result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}