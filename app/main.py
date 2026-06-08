from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 64:
        return False
    try:
        subprocess.run(['ping', host], check=True)
        return True
    except subprocess.CalledProcessError as e:
        return False

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)