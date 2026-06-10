from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., allowed domains or IP addresses
    return host in ['example.com', 'localhost']

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}