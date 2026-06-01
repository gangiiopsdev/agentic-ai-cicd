from fastapi import FastAPI
import subprocess
def execute_safe_command(command: str):
    try:
        result = subprocess.run(command, shell=False, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Command failed with error: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    command = f'ping {host}'
    output = execute_safe_command(command)
    return {"status": "completed", "output": output}