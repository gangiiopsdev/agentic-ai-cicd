from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isdigit():
        raise ValueError("Invalid host")
    args = ["ping", str(host)]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

app = FastAPI()

@app.get="/ping")
def ping(host: str):
    return safe_ping(host)