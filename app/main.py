from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    command = ['ping', host]
    output = subprocess.run(command, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': output.stdout}