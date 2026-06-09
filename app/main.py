from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.strip():
        raise ValueError('Host parameter cannot be empty or consist only of whitespace.')
    command = ['ping'] + shlex.split(host)
    subprocess.run(command, check=True)
    return {"status": "completed"}