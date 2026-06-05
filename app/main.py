from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        # Use shlex.quote to safely escape the input
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)