from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host in ['google.com', 'example.com']:  # Allow only specific hosts for demonstration purposes
        return True
    return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"status": "host_unsafe"}