from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}
    return {'status': 'completed', 'output': output.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)