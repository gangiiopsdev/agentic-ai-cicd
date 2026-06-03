from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent shell injection
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}