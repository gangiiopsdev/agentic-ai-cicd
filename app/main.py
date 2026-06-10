from fastapi import FastAPI
import subprocess
def execute_safe_command(command: str):
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
    # Validate the input to prevent command injection
    allowed_hosts = {'google.com', 'example.com'}
    if host not in allowed_hosts:
        return {"status": "error", "output": "Invalid host"}
    command = f'ping {host}'
    output = execute_safe_command(command)
    return {"status": "completed", "output": output}