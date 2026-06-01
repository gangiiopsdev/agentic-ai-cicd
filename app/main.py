from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex.quote to escape shell characters
    command = ['ping', shlex.quote(host)]
    subprocess.call(command)
    return {'status': 'completed'}