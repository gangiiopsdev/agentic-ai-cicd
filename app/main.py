from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Escape or validate host input to prevent injection attacks
    return ''.join(c for c in host if c.isalnum() or c in ['-', '.', '_'])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', safe_ping(host)])
    return {"status": "completed"}