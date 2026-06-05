from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    if not host.strip():
        raise ValueError('Host parameter cannot be empty')
    # Safe implementation using list for the command and quoting the host
    result = subprocess.run(['ping', quote(host)], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        response = safe_ping(host)
        return {'status': 'completed', 'output': response}
    except ValueError as e:
        return {'error': str(e)}, 400