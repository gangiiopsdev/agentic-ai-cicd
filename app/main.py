from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)