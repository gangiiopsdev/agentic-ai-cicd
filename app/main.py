from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with argument sanitization and input validation
    if not host.replace('.', '').isdigit():
        return {'status': 'error', 'message': 'Invalid host format'}
    args = ['ping', shlex.quote(host)]
    subprocess.call(args)
    return {'status': 'completed'}