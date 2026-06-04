from fastapi import FastAPI
import subprocess
def safe_command(command: str) -> str:
    # Ensure the command does not contain any user-provided input
    allowed_commands = ['ping']
    if command in allowed_commands:
        return command
    else:
        raise ValueError('Command not allowed')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output([safe_command('ping'), host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode('utf-8')}