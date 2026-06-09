from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}