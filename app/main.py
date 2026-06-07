from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using subprocess.run with validation
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError("Invalid hostname")
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}