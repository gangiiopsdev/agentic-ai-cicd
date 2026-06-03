from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'invalid', 'message': 'Invalid host'}
    return execute_ping(host)

def validate_host(host):
    # Add logic to validate the host input
    return True