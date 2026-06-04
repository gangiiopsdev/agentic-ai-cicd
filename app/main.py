from fastapi import FastAPI
import subprocess
import shlex
def execute_safe_command(command, *args):
    safe_args = [shlex.quote(arg) for arg in args]
    result = subprocess.run([command] + safe_args, check=True)
    return result.output  # Capture and handle the output properly

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = execute_safe_command('ping', host)
        return {"status": "completed", "output": result}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}