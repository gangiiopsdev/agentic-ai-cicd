from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    return ['ping', host]

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.run(safe_ping(host), capture_output=True, text=True)
        return {"status": "completed", "output": output.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}