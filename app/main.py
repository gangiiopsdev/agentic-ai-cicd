from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['google.com', 'example.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError("Invalid host")

@app.get("/ping")
def ping(host: str):
    try:
        args = shlex.split('ping ' + host)
        subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": subprocess.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}