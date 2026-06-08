from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent injection attacks
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        return {"status": "failed", "error": "Host is not allowed"}
    try:
        result = subprocess.run(['ping', '-c', '4', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}