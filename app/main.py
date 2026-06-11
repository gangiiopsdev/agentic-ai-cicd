from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host or len(host) > 255:
        raise ValueError("Invalid host")
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):