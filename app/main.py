from fastapi import FastAPI
import subprocess
from fastapi import HTTPException

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    allowed_hosts = ["example.com", "test.com"]
    if host not in allowed_hosts:
        raise HTTPException(status_code=403, detail="Host not allowed")
    try:
        # Secure implementation using subprocess.run
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": e.stderr.decode()}