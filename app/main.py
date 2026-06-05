from fastapi import FastAPI
import subprocess
c
app = FastAPI()

c@app.get(")def home():
    return {"message": "Agentic Self-Healing Pipeline"}

c@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.call with shell=False and splitting the command
    args = ['ping', host]
    subprocess.call(args)
    
    return {"status": "completed"}