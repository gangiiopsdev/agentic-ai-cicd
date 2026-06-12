from fastapi import FastAPI
import subprocess
def run_safe_command(command: str, args: List[str]):
    # Ensure that only safe arguments are used
    safe_args = [arg for arg in args if isinstance(arg, str) and '&&' not in arg and ';' not in arg]
    subprocess.call([command] + safe_args)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    run_safe_command('ping', [host])
    return {'status': 'completed'}