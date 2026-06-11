from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host"}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    # Implement validation logic here
    return host.isdigit() or '.' in host