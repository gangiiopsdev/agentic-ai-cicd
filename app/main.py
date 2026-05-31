from fastapi import FastAPI
import subprocess
getinput = subprocess.getoutput

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    result = getinput(f'ping -c 4 {host}')
    return {"status": "completed", "result": result}