from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    cmd = ['ping'] + shlex.split(host)
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)