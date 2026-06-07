from fastapi import FastAPI
import subprocess
def run_safe_command(command):
    return subprocess.run(command, check=True, capture_output=True, text=True, shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_command = ["ping", host]
    result = run_safe_command(safe_command)
    return {"status": "completed", "output": result.stdout}