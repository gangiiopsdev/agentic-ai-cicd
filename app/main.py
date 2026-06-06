from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_command(command: str):
    try:
        result = subprocess.run(shlex.split(command), capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    result = execute_command(command)
    return {"status": "completed", "result": result}