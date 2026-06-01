from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or not all(c.isalnum() for c in host):
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}