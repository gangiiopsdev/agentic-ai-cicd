from fastapi import FastAPI
import subprocess

app = FastAPI()

def create_ping_command(host):
    return ['ping', host]

@app.get("/ping")
def ping(host: str):

    # Secure implementation with input validation and sanitization
    if not all(c.isalnum() or c in '._-' for c in host) or len(host) > 255:
        raise ValueError('Invalid host name')

    subprocess.call(create_ping_command(host), shell=False)

    return {"status": "completed"}