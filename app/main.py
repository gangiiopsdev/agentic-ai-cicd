from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid input")
    return safe_ping(host)