from fastapi import FastAPI
import subprocess
def run_safe_command(command: str):
    return subprocess.run(command.split(), capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    result = run_safe_command(f"ping {host}")
    return {"status": "completed", "output": result.stdout}