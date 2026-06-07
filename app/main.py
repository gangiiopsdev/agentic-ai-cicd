from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10, shell=False)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return execute_ping(host)

def is_valid_host(host):
    # Implement validation logic to ensure the host is safe to ping
    pass