from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate the host to ensure it does not contain malicious characters or patterns
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "error", "message": "Invalid hostname"}
    subprocess.call(["ping", host])
    return {"status": "completed"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)