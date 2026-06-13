from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}

@app.get("/ping")
def ping(host: str):
    # Validate or sanitize the input to prevent injection attacks
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host'}
    return execute_ping(host)