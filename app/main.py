from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run and shlex.quote
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)