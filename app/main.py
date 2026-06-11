from fastapi import FastAPI
import subprocess
def execute_safe_command(command: str):
    args = shlex.split(command)
    return subprocess.run(args, capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_command = f"ping {host}"
    result = execute_safe_command(safe_command)
    return {"status": "completed", "stdout": result.stdout, "stderr": result.stderr}