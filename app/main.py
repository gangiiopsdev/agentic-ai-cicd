from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command):
    return subprocess.run(command, capture_output=True, text=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    command = ["ping", host]
    result = execute_command(command)
    return {"status": "completed", "output": result.stdout}