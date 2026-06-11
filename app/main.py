from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def execute_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Command failed: {e.stderr}'

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.quote to escape shell metacharacters
    command = ['ping', shlex.quote(host)]
    output = execute_command(command)
    return {"status": "completed", "output": output}