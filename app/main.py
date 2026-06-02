from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host input
    if not is_valid_host(host):
        return {"error": "Invalid host"}, 400
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Basic validation for host input
    return host.strip() and '.' in host