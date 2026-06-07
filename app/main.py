from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Sanitize the host input
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], check=True, timeout=5)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)