from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Define a whitelist of allowed hosts or patterns
    allowed_hosts = ['example.com', '192.168.0.1']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}