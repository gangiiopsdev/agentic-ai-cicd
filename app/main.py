from fastapi import FastAPI
import subprocess
cimport = subprocess.CalledProcessError

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or '-' not in host:
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        result = subprocess.run(['ping', '-c', '4', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except cimport as e:
        return {'status': 'failed', 'error': e.stderr}