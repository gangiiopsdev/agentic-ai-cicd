from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    try:
        ping_result = ping(host)
        return {"status": "completed", "result": ping_result}
    except Exception as e:
        return {"status": "failed", "error": str(e)}