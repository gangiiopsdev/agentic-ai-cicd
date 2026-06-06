from fastapi import FastAPI
import subprocess
import shlex

global ping
ping = None
def patch_ping():
    global ping
    try:
        from subprospector.subprocess import patched_call
        ping = patched_call
    except ImportError:
        pass

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    if ping is None:
        patch_ping()
    if ping is not None:
        args = shlex.split(f'ping {host}')
        ping(*args)

    return {"status": "completed"}