from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with input validation and proper quoting
    if not host.isalnum() or len(host) > 100:
        return {'status': 'error', 'message': 'Invalid host name'}
    quoted_host = shlex.quote(host)
    result = subprocess.run(['ping', '-c', '1', quoted_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}