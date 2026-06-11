from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate and sanitize input
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        raise ValueError('Invalid hostname')
    # Secure implementation
    subprocess.call(['ping', host], shell=False)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return ping(host)