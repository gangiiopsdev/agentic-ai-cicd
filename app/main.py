from fastapi import FastAPI
import subprocess
gl
app = FastAPI()

def execute_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if host.strip() != host:
        raise ValueError('Invalid input')
    command = ["ping", host]
    output = execute_command(command)
    return {"status": "completed", "output": output}