from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate the host to prevent command injection
    if not host or ' ' in host:
        raise ValueError("Invalid host")
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "response": response}