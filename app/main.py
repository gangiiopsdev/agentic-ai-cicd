from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Secure implementation using subprocess.run with a list of arguments to avoid shell injection
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr.decode()}

@app.get("/ping")
def ping_route(host: str):
    # Validate input to ensure it is a valid hostname
    if not host.isalnum() and '-' not in host and '.' not in host:
        raise ValueError("Invalid hostname")
    return ping(host)