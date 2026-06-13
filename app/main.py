from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isdigit():
        return 'Invalid input'
    subprocess.call(['ping', host])
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": result}