from fastapi import FastAPI
import subprocess
def run_safe_command(command: str, args: List[str]):
    # Ensure that only safe arguments are used
    safe_args = [arg for arg in args if isinstance(arg, str) and '&&' not in arg and ';' not in arg]
    try:
        result = subprocess.run([command] + safe_args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Command failed: {e}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return run_safe_command('ping', [host])