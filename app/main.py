from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Sanitize and split host to prevent command injection
    safe_host = shlex.quote(host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        subprocess.call(['ping', safe_host])
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}
    return {'status': 'completed'}