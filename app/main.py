from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize host input
    if ' ' in host or ';' in host or '&' in host or '|' in host:
        return {'error': 'Invalid host input'}
    subprocess.call(["ping", host])
    return {"status": "completed"}