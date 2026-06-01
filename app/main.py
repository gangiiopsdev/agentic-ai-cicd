from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and avoiding shell=True
    if not is_valid_host(host):
        return {'error': 'Invalid host'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

# Helper function to validate the host input
def is_valid_host(host: str) -> bool:
    # Basic validation to prevent command injection
    return all(c not in host for c in [';', '&', '|', '<', '>', '*', '?', '~', '`'])