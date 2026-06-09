from fastapi import FastAPI
import subprocess
import shlex

def execute_safe_command(command: str):
    try:
        args = shlex.split(command)
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if host not in ['google.com', 'example.com']:
        return {'status': 'error', 'output': 'Invalid host'}
    command = f'ping {host}'
    output = execute_safe_command(command)
    return {'status': 'completed', 'output': output}