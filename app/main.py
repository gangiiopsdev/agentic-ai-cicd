from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

def validate_host(host: str) -> bool:
    try:
        result = urlparse(host)
        return all([result.scheme, result.netloc])
    except Exception as e:
        return False

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host format"}
    try:
        # Secure implementation
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": subprocess.PIPE.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}