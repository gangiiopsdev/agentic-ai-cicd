from fastapi import FastAPI
import subprocess
def execute_safe_command(command, args):
    completed_process = subprocess.run([command] + list(args), capture_output=True, text=True)
    return completed_process.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = execute_safe_command("ping", [host])
    return {"status": "completed", "result": result}