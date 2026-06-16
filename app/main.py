from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate the host input to avoid injection attacks
    if not all(c.isalnum() or c in '.-' for c in host):
        return {'status': 'failed', 'error': 'Invalid host format'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)