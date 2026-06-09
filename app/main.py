from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.strip().isalnum() or len(host) > 255:
        raise ValueError('Invalid hostname')
    result = subprocess.run(['ping', '-c', '1', shlex.quote(host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}