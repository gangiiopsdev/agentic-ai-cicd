from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_safe_command(command: str):
    try:
        result = subprocess.run(command.split(), check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    result = run_safe_command(command)
    return {"status": "completed", "result": result}