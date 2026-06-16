from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with absolute path to prevent command injection
    subprocess.run(['/bin/ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)