from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation with validation
    if host.strip().endswith('.localdomain'):
        subprocess.call(['ping', host])

@app.get("/ping")
def ping_endpoint(host: str):
    result = ping(host)
    return {'status': 'completed'}