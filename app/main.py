from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        subprocess.call(['ping', host], timeout=5)
        return True
    except Exception as e:
        print(e)
        return False

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed", "result": "success"}
    else:
        return {"status": "failed", "result": "failure"}