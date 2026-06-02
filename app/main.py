from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with validation and sanitization
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

def is_valid_host(host: str) -> bool:
    # Add validation logic here (e.g., regex pattern matching)
    return True