from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize the host input
    if not isinstance(host, str) or not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_ping(host)