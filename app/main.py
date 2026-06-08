from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Add more as needed
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    command = ['ping', host]
    args = shlex.split(' '.join(command))
    subprocess.run(args, check=True)
    return {"status": "completed"}