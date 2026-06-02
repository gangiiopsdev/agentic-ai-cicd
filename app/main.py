from fastapi import FastAPI
import subprocess
cimport = {"ping": "ping -c 1 {}"}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = cimport.get('ping'.lower())
    if command:
        subprocess.call(command.format(host), shell=True)
    return {"status": "completed"}