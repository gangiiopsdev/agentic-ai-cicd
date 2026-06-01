from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_host(host):
    return ''.join(c for c in host if c.isalnum() or c in ['.', '-', '_'])

@app.get("/ping")
def ping(host: str):
    safe_host_value = safe_host(host)
    command = ['ping', safe_host_value]
    subprocess.run(command, check=True)
    return {"status": "completed"}