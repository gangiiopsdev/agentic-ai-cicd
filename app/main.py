from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    command_parts = ["ping", host]
    output = execute_safe_command(command_parts)
    return {"status": "completed", "output": output}