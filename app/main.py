from fastapi import FastAPI
import subprocess
global_result = None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global global_result
    result = subprocess.call(['ping', host], capture_output=True, text=True)
    global_result = result.stdout
    return {"status": "completed", "output": global_result}