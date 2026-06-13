from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_safe_command(command, *args):
    # Validate and sanitize user input
    for arg in args:
        if isinstance(arg, str) and not all(c.isalnum() or c.isspace() for c in arg):
            raise ValueError('Invalid characters in command argument')
    return subprocess.run([command] + list(args), capture_output=True, text=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with input validation
    result = execute_safe_command('ping', host)
    return {'status': 'completed', 'output': result.stdout}