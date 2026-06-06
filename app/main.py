from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command: list):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Command failed with error code {e.returncode}: {e.stderr}"

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in ['127.0.0.1', '::1']:
        return {'status': 'completed', 'output': 'Invalid host'}
    command = ['ping', host]
    result = execute_command(command)
    return {'status': 'completed', 'output': result}