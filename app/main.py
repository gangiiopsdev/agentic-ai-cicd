from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        subprocess.run(['ping', host], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e}')
        return False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_input(host):
        return {"status": "failed", "reason": "Invalid or malicious input detected."}
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed"}