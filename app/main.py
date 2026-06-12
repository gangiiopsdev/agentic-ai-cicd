from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use subprocess.run to avoid shell injection
    try:
        subprocess.run(['ping', host], check=True, timeout=5)
    except subprocess.CalledProcessError as e:
        return False, str(e)
    return True, "Completed"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    success, message = safe_ping(host)
    if success:
        return {"status": message}
    else:
        return {"error": message}