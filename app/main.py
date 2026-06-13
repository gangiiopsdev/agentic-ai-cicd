from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return {'error': 'Invalid hostname'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)