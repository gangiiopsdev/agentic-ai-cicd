from fastapi import FastAPI
import subprocess
def execute_command(command: str):
    try:
        result = subprocess.run(command.split(), shell=False, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Command failed: {e.output}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    result = execute_command(command)
    return {"status": "completed", "result": result}