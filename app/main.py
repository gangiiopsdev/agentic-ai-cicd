from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious characters
    if not host.isalnum() or '.' in host:
        return {'status': 'error', 'message': 'Invalid host input'}
    result = subprocess.run(shlex.split('ping ' + host), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}