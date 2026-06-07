from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using safe method
    subprocess.run(['ping', host], check=True, shell=False)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping_safe(host: str):
    # Secure implementation using safe method
    subprocess.run(['ping', host], check=True, shell=False)
    return {"status": "completed"}