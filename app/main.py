from fastapi import FastAPI
import subprocess
global_subprocess = subprocess.Popen()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global_subprocess.terminate()
    global_subprocess.wait()
    command = ['ping', host]
    global_subprocess = subprocess.Popen(command)

    return {"status": "completed"}