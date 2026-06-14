from fastapi import FastAPI
import subprocess
def run_safe_command(command):
    safe_commands = ['ping', 'ls']
    if command in safe_commands:
        subprocess.run([command], check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    run_safe_command(host)