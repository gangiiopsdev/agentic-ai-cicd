from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Simple validation for demonstration purposes
    return host.strip().replace('.', '').isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    command = ['ping', '-c', '1']  # Use specific options to mitigate risks
    subprocess.run(command, args=[host], check=True)
    return {"status": "completed"}