from fastapi import FastAPI
import subprocess
import shlex

global_app = None

app = FastAPI()

@app.on_event("startup")
def startup():
    global global_app
    global_app = app

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent shell injection
    allowed_hosts = ["example.com", "another-example.com"]
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
    command = shlex.split(f'ping {host}')
    subprocess.run(command, check=True)
    return {"status": "completed"}