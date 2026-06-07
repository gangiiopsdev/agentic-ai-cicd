from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"status": "error", "message": "Invalid host"}
    command = ['ping', host]
    subprocess.run(command, capture_output=True, text=True)
    return {"status": "completed"}