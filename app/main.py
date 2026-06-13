from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

def validate_host(host):
    try:
        result = urlparse(host)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "failed", "error": "Invalid host"}