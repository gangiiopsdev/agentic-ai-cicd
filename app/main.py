from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return output.stdout.strip()
    except subprocess.CalledProcessError as e:
        return str(e.stderr.strip())

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}