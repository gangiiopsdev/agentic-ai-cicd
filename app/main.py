from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if host in ['127.0.0.1', 'localhost']:  # Add additional allowed hosts as needed
        try:
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
            return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}
    else:
        return {'status': 'denied', 'error': 'Invalid host'}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)