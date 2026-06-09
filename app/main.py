from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Sanitize the input to avoid shell injection
    args = ['ping'] + shlex.split(host)
    return args

def run_safe_command(command_args: list):
    try:
        subprocess.run(command_args, check=True, capture_output=True, text=True)
        return "Command executed successfully"
    except subprocess.CalledProcessError as e:
        return f"Command failed: {e.stderr}"

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = safe_ping(host)
    result = run_safe_command(safe_host)
    return {"status": "completed", "result": result}