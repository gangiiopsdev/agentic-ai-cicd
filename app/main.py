from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.startswith(('127.0.0.1', '::1')):
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "output": result}