from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    # Validate the host input to ensure it is safe
    if not host.isalnum():
        raise ValueError('Invalid host input')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}