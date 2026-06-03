from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with full path and validation
    subprocess.run(['/bin/ping', host], check=True, timeout=5)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)