from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.isnumeric():
        return subprocess.run(['ping', host], capture_output=True, text=True)
    else:
        raise ValueError('Invalid input for ping')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "output": result.stdout}
    except ValueError as e:
        return {"error": str(e)}