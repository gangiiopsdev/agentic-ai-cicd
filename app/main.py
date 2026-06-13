from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Using subprocess.run with list argument for safer execution
    subprocess.run(['ping', host], check=True)

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