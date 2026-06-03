from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with full command
    subprocess.run(['ping', '-c', '1', host], check=True)

@app.get("/ping")
def ping_host(host: str):
    return ping(host)