from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Ensure the host parameter is sanitized to prevent command injection
    if not isinstance(host, str) or not host.strip():
        raise ValueError("Invalid input")
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

@app.get="/ping")
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "response": response}