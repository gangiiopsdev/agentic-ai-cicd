from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host in ['127.0.0.1', 'localhost']:
        command = ['ping', host]
        result = subprocess.run(command, check=True, capture_output=True)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.run(['ping', host], check=True, capture_output=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'stderr': e.stderr.decode()}