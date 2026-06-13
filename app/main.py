from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Replace with a safe implementation that avoids shell=True
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}