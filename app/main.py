from fastapi import FastAPI
import subprocess
global ping

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed"}