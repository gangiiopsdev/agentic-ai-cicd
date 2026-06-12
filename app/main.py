from fastapi import FastAPI
import subprocess
def execute_safe_command(command):
    try:
        result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_command = f'ping {host.strip()}'  # Sanitize input by stripping whitespace
    result = execute_safe_command(safe_command)
    return {"status": result}