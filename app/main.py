from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['example.com', 'localhost']  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    result = subprocess.run(['ping', host], shell=False, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)