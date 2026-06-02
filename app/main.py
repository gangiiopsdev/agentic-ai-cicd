from fastapi import FastAPI
import subprocess
def execute_safe_command(command):
    try:
        output = subprocess.run(command, check=True, capture_output=True, text=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Command failed: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    result = execute_safe_command(command)
    return {"status": "completed", "result": result}