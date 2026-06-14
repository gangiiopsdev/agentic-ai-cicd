from fastapi import FastAPI
import subprocess
def run_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_command_parts = ['ping', host]
    return run_safe_command(safe_command_parts)