from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Input validation and sanitization
    if not host.strip():
        return {'error': 'Invalid input'}
    return execute_ping(host)