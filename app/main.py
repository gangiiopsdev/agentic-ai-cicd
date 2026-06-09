from fastapi import FastAPI
import subprocess
def execute_safe_command(command_parts):
    subprocess.run(command_parts, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command_parts = ["ping", host]
    execute_safe_command(command_parts)
    return {"status": "completed"}