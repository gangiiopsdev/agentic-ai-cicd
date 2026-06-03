from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not all(c.isalnum() or c in ['-', '.', '_', ':'] for c in host):
        return {"error": "Invalid hostname"}, 400
    
    # Using safe function to prevent command injection
    safe_ping(host)

    return {"status": "completed"}