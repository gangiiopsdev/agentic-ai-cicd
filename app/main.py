from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    return all(c.isalnum() or c in ('.', '-') for c in host)

@app.get("/ping")
def ping(host: str):
    if is_valid_host(host):
        command = shlex.split(f"ping {host}")
        subprocess.call(command)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 400