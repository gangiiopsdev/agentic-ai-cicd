from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., check if the host is allowed
    return True

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}