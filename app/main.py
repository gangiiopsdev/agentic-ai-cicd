from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation and sanitization
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        subprocess.call(['ping', host])
    else:
        return {'error': 'Invalid host'}
    return {'status': 'completed'}