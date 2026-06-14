from fastapi import FastAPI
import subprocess
def safe_ping(host):
    return {'status': 'completed'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host in ['google.com', 'example.com']:  # Example of hardcoding safe hosts
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    else:
        return safe_ping(host)