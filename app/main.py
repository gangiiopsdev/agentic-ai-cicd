from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host):
    return host.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    command = f"ping {escape_host(host)}"
    args = shlex.split(command)
    subprocess.call(args, shell=False)
    return {"status": "completed"}