from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.run(shlex.split(f'ping {host}'), check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 400