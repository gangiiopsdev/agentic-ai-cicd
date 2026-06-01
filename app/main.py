from fastapi import FastAPI
import subprocess
from os.path import abspath, dirname, join

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = subprocess.quote(host)
    subprocess.run([abspath(join(dirname(__file__), 'ping')), safe_host], check=True)
    return {"status": "completed"}