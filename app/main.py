from fastapi import FastAPI
import subprocess
def execute_safe_command(command_args):
    try:
        result = subprocess.run(command_args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.returncode}
Stderr: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command_args = ["ping", host]
    result = execute_safe_command(command_args)
    return {"status": "completed", "result": result}