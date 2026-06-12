from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    cmd = ["ping", host]
    result = run_command(cmd)
    return {"status": "completed", "output": result}