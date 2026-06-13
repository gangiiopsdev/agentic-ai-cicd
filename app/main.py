from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Add input validation here
    if not host.strip():
        return {'status': 'failed', 'error': 'Invalid input'}
    return execute_ping(host)