from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and validation
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        return {'error': 'Invalid host'}

    try:
        result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': 'Ping failed', 'output': e.stderr}