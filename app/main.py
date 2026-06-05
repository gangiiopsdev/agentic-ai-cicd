from fastapi import FastAPI
import subprocess

app = FastAPI()

global_host = 'example.com' # Ensure this is sanitized

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}