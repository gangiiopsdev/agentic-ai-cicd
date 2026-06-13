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
        subprocess.call(['ping', '-c', '1', safe_host])  # Use '-c' option for limiting the number of pings
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}
    return {'status': 'completed'}