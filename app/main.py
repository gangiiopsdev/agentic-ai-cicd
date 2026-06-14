from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    # Implement a safe host check here
    return True if host in ['example.com', 'localhost'] else False

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Invalid host")
    command = shlex.split('ping ' + host)
    subprocess.run(command, check=True)
    return {"status": "completed"}