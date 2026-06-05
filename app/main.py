from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate input
    if any(char in host for char in [';', '|', '&', '`']):
        return {"status": "error", "message": "Invalid input"}
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "success", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)