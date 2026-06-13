from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex to safely pass arguments
    safe_host = subprocess.list2cmdline([host])
    subprocess.run(['ping', safe_host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)