from fastapi import FastAPI
import subprocess

def execute_safe_command(command: str, args: list):
    try:
        result = subprocess.run([command] + args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_command = ['ping']
    if host:
        safe_command.append(host)
    # Sanitize input to prevent command injection
    if not all(c.isalnum() or c in '-.' for c in ''.join(safe_command)):
        return {'status': 'failed', 'error': 'Invalid input'}
    return execute_safe_command('ping', safe_command)