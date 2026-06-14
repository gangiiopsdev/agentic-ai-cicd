from fastapi import FastAPI
import subprocess

app = FastAPI()

def create_ping_command(host):
    return ['ping', host]

@app.get("/ping")
def ping(host: str):

    # Secure implementation with input validation
    if not all(c.isalnum() or c in '._-' for c in host):
        raise ValueError('Invalid host name')

    subprocess.call(create_ping_command(host), shell=False)

    return {"status": "completed"}