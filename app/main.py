from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize the host input to prevent command injection
        safe_host = subprocess.list2cmdline([host])
        subprocess.call(["ping", safe_host], shell=False)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500