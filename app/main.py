from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum() or len(host) > 15:
        return {'status': 'error', 'message': 'Invalid host' }
    safe_host = shlex.quote(host)
    subprocess.call(['ping', safe_host])
    return {'status': 'completed'}