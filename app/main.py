from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Basic validation to ensure the host contains only valid characters
    return all(c.isalnum() or c in '.-[]' for c in host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'error': 'Invalid host'}
    result = subprocess.run(['ping', '-c', '1', quote(host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}