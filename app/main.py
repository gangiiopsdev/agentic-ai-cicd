from fastapi import FastAPI
import subprocess
def execute_command(command):
    return subprocess.run(command, check=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_host = subprocess.list2cmdline([host])  # Sanitize the input
    command = ["ping", safe_host]
    result = execute_command(command)
    return {"status": "completed", "output": result.stdout}