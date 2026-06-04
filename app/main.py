from fastapi import FastAPI
import subprocess
def run_safe_command(command, args):
    # Use subprocess.run instead of subprocess.call and avoid using shell=True
    return subprocess.run([command] + args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Run the ping command safely without shell=True
    run_safe_command("ping", [host])
    return {"status": "completed"}