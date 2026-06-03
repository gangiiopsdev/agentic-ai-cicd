from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not host.strip():
        return {'status': 'error', 'message': 'Invalid host'}
    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', '-c', '4', safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}