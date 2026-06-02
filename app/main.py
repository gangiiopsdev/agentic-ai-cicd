from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, timeout=5, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e.stdout}\n{e.stderr}')
        return False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host.replace(';', '').replace('&', '')):
        return {"status": "completed"}
    else:
        return {"status": "failed"}