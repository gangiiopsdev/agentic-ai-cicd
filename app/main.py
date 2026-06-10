from fastapi import FastAPI
import subprocess
def execute_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    command_parts = ["ping", host]
    result = execute_safe_command(command_parts)
    return {"status": "completed", "output": result}