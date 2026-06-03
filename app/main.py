from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation to avoid shell injection and ensure safe execution
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {"status": "completed"}