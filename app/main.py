from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation without shell=True
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in ('-', '.', '_') for c in host):  # Basic validation of host input
        return {'status': 'error', 'message': 'Invalid host'}
    safe_ping(host)
    return {'status': 'completed'}