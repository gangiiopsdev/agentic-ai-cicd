from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use subprocess.run to avoid shell injection
    try:
        result = subprocess.run(['ping', host], check=True, timeout=5, capture_output=True, text=True)
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return False, str(e.stderr.strip())

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