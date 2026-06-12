from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command):
    # Safe implementation using subprocess.run
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return result.stdout

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    output = execute_command(command)
    return {"status": "completed", "output": output}