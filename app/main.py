from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.isalnum() and '.' in host:
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], timeout=5, stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)