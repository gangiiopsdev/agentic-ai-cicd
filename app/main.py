from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command_parts = shlex.split(f"ping {host}")
    result = run_command(command_parts)
    return {"status": "completed", "result": result}