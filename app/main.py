from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host: str):
    if not host.isdigit():
        raise ValueError('Invalid host format')

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = ['ping', shlex.quote(host)]
    subprocess.call(command, shell=False)

    return {"status": "completed"}