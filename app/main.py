from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent injection attacks
    allowed_hosts = ["example.com", "test.com"]
    if host in allowed_hosts:
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"error": "Host not allowed"}