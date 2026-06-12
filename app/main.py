from fastapi import FastAPI
import subprocess
def execute_command(command: str):
    parts = command.split()
    process = subprocess.Popen(parts, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

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
        return {"status": "failed", "error": error.decode()}
    else:
        return {"status": "completed", "output": output.decode()}