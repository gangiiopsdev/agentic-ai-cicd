from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic validation: check if host contains only allowed characters
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        raise ValueError('Invalid hostname')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}