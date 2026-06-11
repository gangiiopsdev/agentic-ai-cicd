from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and argument unpacking
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}