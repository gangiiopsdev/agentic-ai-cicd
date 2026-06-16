from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_hostname(hostname: str) -> bool:
    return hostname.isalnum() and len(hostname) <= 255

@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        raise ValueError("Invalid hostname")
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}