from fastapi import FastAPI
import subprocess
from shlex import quote
def ping(host: str):
    # Secure implementation using subprocess.run and shlex.quote
    try:
        result = subprocess.run(['ping', quote(host)], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

app = FastAPI()

@app.get('/ping')
def ping_route(host: str):
    return ping(host)