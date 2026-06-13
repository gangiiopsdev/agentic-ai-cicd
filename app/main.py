from fastapi import FastAPI
import subprocess
def execute_safe_command(command, *args):
    # Ensure that only safe commands are executed
    allowed_commands = ['ping']
    if command in allowed_commands:
        return subprocess.run([command] + list(args), check=True)
    else:
        raise ValueError(f'Unsupported command: {command}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    execute_safe_command('ping', host)
    return {"status": "completed"}