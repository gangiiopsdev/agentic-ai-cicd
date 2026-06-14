from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    # Simple validation, replace with more robust logic
    return host.replace('.', '').isdigit()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"error": "Invalid host"}, 400
    args = shlex.split('ping ' + host)
    subprocess.call(args)
    return {"status": "completed"}