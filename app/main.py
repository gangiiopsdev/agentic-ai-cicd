from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.call with shell=False
    try:
        subprocess.call(['ping', host], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    except Exception as e:
        return {"error": str(e)}

    return {"status": "completed"}