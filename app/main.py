from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Sanitize the host input to prevent injection attacks
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        return {'error': 'Invalid host'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if 'error' in result:
        return result
    subprocess.call(['ping', host])
    return {"status": "completed"}