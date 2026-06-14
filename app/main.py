from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "error", "message": "Invalid host"}
    safe_ping(host)
    return {"status": "completed"}