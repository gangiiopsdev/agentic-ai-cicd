from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def secure_ping(host: str):
    if not host.isdigit() or len(host) < 3 or len(host) > 15:
        return {"status": "error", "output": "Invalid host format"}
    result = ping(host)
    return {"status": "completed", "output": result}