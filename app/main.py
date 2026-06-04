from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and validation
    if host.strip() and all(c.isalnum() or c in '.-:' for c in host):  # Simple validation example
        command = ['ping', '-c', '1', shlex.quote(host)]
        subprocess.run(command, check=True)
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid hostname')