from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or not all(c.isalnum() for c in host):
        raise ValueError('Invalid host name')
    try:
        output = subprocess.run(['ping', '-c', '1', os.path.basename(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}