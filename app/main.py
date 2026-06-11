from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent injection attacks
    if host and all(c.isalnum() or c in ('.', '-', '_') for c in host):
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid host name')

    return {"status": "completed"}