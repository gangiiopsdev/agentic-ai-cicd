from fastapi import FastAPI
import subprocess
def safe_execute(command: str):
    try:
        # Use a whitelist of allowed commands and arguments
        allowed_commands = ['ping']
        if command.split()[0] in allowed_commands:
            result = subprocess.run(command.split(), capture_output=True, check=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            raise ValueError('Unauthorized command')
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_command = f'ping {host}'
    return safe_execute(safe_command)