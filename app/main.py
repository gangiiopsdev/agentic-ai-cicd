from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not valid_host(host):
        return {'status': 'invalid', 'message': 'Invalid host'}
    return safe_ping(host)
def valid_host(host: str) -> bool:
    # Add validation logic for the host
    return True