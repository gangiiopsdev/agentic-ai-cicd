from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_host(host: str):
    return ping(host)