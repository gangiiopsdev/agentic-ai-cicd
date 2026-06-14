from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using list of arguments and shell escaping
    subprocess.run(['ping', quote(host)])

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():  # Basic validation to prevent injection
        return {'status': 'error', 'message': 'Invalid input'}
    safe_ping(host)
    return {'status': 'completed'}