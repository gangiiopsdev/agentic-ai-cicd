from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        subprocess.run(['ping', host], check=True, timeout=5)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')
        return False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed"}