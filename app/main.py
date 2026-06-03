from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.isdigit():
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '1'] + shlex.split(host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)