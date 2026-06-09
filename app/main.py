from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

def validate_host(host):
    result = urlparse(host)
    return bool(result.scheme and result.netloc)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        output = subprocess.run(['ping', '-c 4', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}