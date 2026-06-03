from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation with validation and sanitization
    if not host.isalnum() or len(host) > 50:
        return False
    return True

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"status": "failed", "error": "Invalid host name"}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}