from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate input to prevent command injection
    if 'ping' not in host:
        raise ValueError('Invalid input')
    result = subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed', 'output': result.stdout.decode('utf-8')}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)