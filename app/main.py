from fastapi import FastAPI
import subprocess

def safe_subprocess(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

app = FastAPI()
@app.get("/run_command/")
def run_command(command: str):
    # Validate and sanitize input
    safe_command = [arg.strip() for arg in command.split()] if isinstance(command, str) else []
    return safe_subprocess(safe_command)