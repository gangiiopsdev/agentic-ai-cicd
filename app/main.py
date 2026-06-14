from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    valid_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host not in valid_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)