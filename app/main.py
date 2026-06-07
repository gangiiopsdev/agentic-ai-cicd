from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with shlex.quote to prevent command injection
    subprocess.call(['ping', shlex.quote(host)])
    return {"status": "completed"}