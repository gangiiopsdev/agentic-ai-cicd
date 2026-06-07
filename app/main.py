from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation with input validation
    if not host or not host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}