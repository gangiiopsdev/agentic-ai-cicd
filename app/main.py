from fastapi import FastAPI
import subprocess
def execute_safe_command(command, *args):
    return subprocess.run([command] + list(args), capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    result = execute_safe_command("ping", host)
    return {"status": "completed", "output": result.stdout}