from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command):
    args = command.split()
    return subprocess.run(args, capture_output=True, text=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    result = execute_command(f"ping {host}")

    return {"status": "completed", "output": result.stdout}