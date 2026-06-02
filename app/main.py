from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError("Invalid host")
    subprocess.run(["ping", f'"{host}"'], check=True)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)