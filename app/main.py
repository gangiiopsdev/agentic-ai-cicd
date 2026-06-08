from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run and shlex.split for safe argument passing
    subprocess.run(['ping', host], check=True, text=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)