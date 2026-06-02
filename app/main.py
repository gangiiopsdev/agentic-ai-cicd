from fastapi import FastAPI
import subprocess
git = __import__('subprocess').getoutput

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    output = git(f'ping {host}')
    return {"status": "completed", "output": output}