from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    if host.strip() not in ['127.0.0.1', '::1']:  # Allow only localhost addresses for safety
        return {"status": "invalid_host"}
    command_parts = shlex.split(f'ping {host}')
    subprocess.run(command_parts, check=True)
    return {"status": "completed"}

@app.get("/ping")
def ping_wrapper(host: str):
    return ping(host)