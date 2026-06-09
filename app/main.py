from fastapi import FastAPI
import subprocess
def secure_ping(host):
    # Secure implementation
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)