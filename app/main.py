from fastapi import FastAPI
import subprocess
def execute_safe_command(command):
    try:
        # Validate the command input
        for arg in command:
            if not isinstance(arg, str) or '&&' in arg or ';' in arg or '|' in arg:
                raise ValueError('Invalid command arguments')
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Command failed: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    return execute_safe_command(command)