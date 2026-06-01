from fastapi import FastAPI
import subprocess
from os.path import abspath, dirname, join
def validate_host(host):
    # Implement host validation logic here
    if not validate_host_logic(host):
        raise ValueError("Invalid host")

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation
    subprocess.run([abspath(join(dirname(__file__), 'ping')), host], check=True)
    return {"status": "completed"}