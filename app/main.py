from fastapi import FastAPI
import subprocess
global process

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global process
    if process:
        process.terminate()
    process = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return {"status": "completed", "output": process.communicate()}

@app.on_event("shutdown")
def stop_ping():
    global process
    if process:
        process.terminate()