from fastapi import FastAPI
import subprocess
gateway = subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = gateway.stdout if gateway.returncode == 0 else gateway.stderr
    return {"status": result}