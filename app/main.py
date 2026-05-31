from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to avoid injection
    allowed_hosts = ["example.com", "test.example.com"]
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}