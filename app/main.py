from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host: str):
    # Secure implementation using subprocess.run with proper validation and sanitization
    if not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    response = _ping(host)
    return {"status": "completed", "output": response}