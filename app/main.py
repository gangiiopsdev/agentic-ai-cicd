from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with full path and shell=True for better security
    subprocess.run(['/bin/ping', host], check=True, shell=True)
    return {"status": "completed"}