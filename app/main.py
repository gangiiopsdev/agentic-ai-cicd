from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using check_output and avoiding shell=True
    subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}