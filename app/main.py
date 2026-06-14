from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid input')
    # Secure implementation
    try:
        output = subprocess.run(['ping', '-c', '1'] + shlex.split(shlex.quote(host)), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid input')
    return ping(host)