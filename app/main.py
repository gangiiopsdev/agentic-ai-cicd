from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    # Validate the input before executing the subprocess
    validate_host(host)
    result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}