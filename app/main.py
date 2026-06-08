from fastapi import FastAPI
import subprocess
from shlex import quote

def execute_safe_command(command_parts):
    try:
        quoted_command = ' '.join(quote(part) for part in command_parts)
        result = subprocess.run(quoted_command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command_parts = ["ping", host]
    output = execute_safe_command(command_parts)
    return {"status": "completed", "output": output}