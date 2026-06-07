from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        subprocess.call(['ping', host])
        return True
    except Exception as e:
        print(e)
        return False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed"}