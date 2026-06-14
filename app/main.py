from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command, args):
    # Secure implementation using a whitelist and validation
    allowed_commands = ['ping']
    if command not in allowed_commands:
        raise ValueError(f'Command {command} is not allowed')
    full_command = [command] + list(shlex.split(args))
    return subprocess.call(full_command, shell=False)

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Secure implementation
    return run_command('ping', host)