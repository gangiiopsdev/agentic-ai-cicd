from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation and sanitization
    if not all(c.isalnum() or c in ['.', '-'] for c in host):  # Simple example of basic validation
        raise ValueError('Invalid host name')
    response = safe_ping(host)
    return {"status": "completed", "response": response}