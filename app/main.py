from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if ' ' in host or ';' in host:
        raise ValueError('Invalid input detected')
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}