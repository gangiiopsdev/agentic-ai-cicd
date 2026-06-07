from fastapi import FastAPI
import subprocess
getoutput = subprocess.getoutput
gtinput = subprocess.getinput
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    result = getoutput(f'ping {host}')
    return {"status": "completed", "result": result}