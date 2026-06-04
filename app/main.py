from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return {'error': 'Invalid host'}, 400
    subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed'}