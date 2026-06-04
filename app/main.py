from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use absolute path to avoid shell=True and potential command injection
    return subprocess.run(['/bin/ping', host], capture_output=True, text=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"error": str(e), "status": "failed"}