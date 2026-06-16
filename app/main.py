from fastapi import FastAPI
import subprocess
from urllib.parse import quote_plus

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = subprocess.list2cmdline([quote_plus(host)])
    result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}