from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', '-c', '1', host])  # Limit the number of pings to avoid excessive resource usage
    return {"status": "completed"}