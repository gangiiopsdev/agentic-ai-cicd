from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    command = f'ping {host}'
    result = execute_command(command)
    return {'status': 'completed', 'result': result}

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

def execute_command(command: str):
    try:
        result = subprocess.run(shlex.split(command), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)