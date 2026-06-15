from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.strip():
        raise ValueError('Host cannot be empty')
    try:
        # Safe implementation using subprocess.run
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    response = safe_ping(host)
    return {"status": "completed", "response": response}