from fastapi import FastAPI
import subprocess

def validate_host(host: str):
    # Implement a more robust validation logic
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/health")
def health_check():
    return {'status': 'ok'}