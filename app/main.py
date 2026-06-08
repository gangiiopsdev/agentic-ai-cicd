from fastapi import FastAPI
import subprocess
def run_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid host name")
    safe_command = ['ping', host]
    output = run_safe_command(safe_command)
    return {"status": "completed", "output": output}