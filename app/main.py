from fastapi import FastAPI
import subprocess
global_result = None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global_result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": global_result.stdout}