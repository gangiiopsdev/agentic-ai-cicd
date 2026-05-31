from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        # Validate and sanitize the host input
        if not is_valid_host(host):
            raise ValueError('Invalid host')
        host = shlex.quote(host)
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return f'Error: {e}'

app = FastAPI()

def is_valid_host(host: str):
    # Implement validation logic here
    return True

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}