from fastapi import FastAPI
import subprocess
global_ping_enabled = True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent code injection
    if not global_ping_enabled or not host.isdigit() or len(host) != 3:
        raise ValueError("Invalid host address")
    subprocess.call(["ping", host])
    return {"status": "completed"}