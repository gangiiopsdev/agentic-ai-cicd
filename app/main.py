from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Ensure the host parameter is sanitized or limited to trusted values
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return {"status": "failed", "message": "Unauthorized host"}

    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)