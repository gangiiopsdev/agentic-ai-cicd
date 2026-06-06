from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run with shlex.split for argument parsing
    args = ['ping', host]
    for arg in args:
        if ' ' in arg or '	' in arg or '\' in arg or ';' in arg or '&' in arg or '|' in arg:
            raise ValueError('Invalid characters in hostname')
    subprocess.run(args, shell=False)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}