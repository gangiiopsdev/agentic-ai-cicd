from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host: str):
    try:
        args = ['ping', shlex.quote(host)]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}''

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isdigit() or len(host) > 15:
        return {'error': 'Invalid host provided'}
    return safe_ping(host)