from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        raise ValueError('Invalid host name')

    # Secure implementation using shlex.quote
    subprocess.run(['ping', shlex.quote(host)], check=True, shell=False)

    return {'status': 'completed'}