from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize input to prevent command injection
    if host.strip() != host:
        raise ValueError('Invalid host input')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_handler(host: str):
    return ping(host)