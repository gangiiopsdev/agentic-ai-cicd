from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation without using shell=True and validate input
    args = ['ping', host]
    if not is_valid_host(host):
        return {'status': 'error', 'output': 'Invalid host'}
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

def is_valid_host(host: str) -> bool:
    # Basic validation to avoid injection
    return all(c.isalnum() or c in ('-', '.', '_') for c in host)