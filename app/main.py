from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Using subprocess.run for a safer approach
    try:
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e.stdout}')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed", "host": host}