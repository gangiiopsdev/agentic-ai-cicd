from fastapi import FastAPI
import subprocess
def run_safe_command(command):
    if command in ['ping', 'ls']:
        subprocess.call(['sudo', command])
app = FastAPI()
@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get="/ping"
def ping(host: str):
    return run_safe_command(host)