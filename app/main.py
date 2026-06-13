from fastapi import FastAPI
import subprocess
def execute_command(command: str):
    parts = command.split()
    process = subprocess.run(parts, capture_output=True, text=True)
    return process.stdout, process.stderr

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    command = f'ping {host}'
    output, error = execute_command(command)
    if error:
        return {"status": "failed", "error": error}
    else:
        return {"status": "completed", "output": output}