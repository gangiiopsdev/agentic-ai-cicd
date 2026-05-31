from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.Popen to avoid shell=True
    command = ['ping', host]
    subprocess.call(command, shell=False)
    return {"status": "completed"}