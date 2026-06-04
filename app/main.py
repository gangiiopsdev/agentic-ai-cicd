from fastapi import FastAPI
import subprocess
def execute_command(command):
    return subprocess.run(command, capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ["ping", host.strip()]  # Remove any leading/trailing whitespace from user input
    result = execute_command(command)
    return {"status": "completed", "output": result.stdout}