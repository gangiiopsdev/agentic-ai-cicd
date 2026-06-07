from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use subprocess.run with list to avoid shell injection
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)