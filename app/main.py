from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    command = ['ping', '-c 1', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}