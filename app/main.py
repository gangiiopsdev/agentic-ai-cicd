from fastapi import FastAPI
import subprocess
def generate_ping_command(host):
    return f'ping {host}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it's safe for a ping command
    if not is_safe_for_ping(host):
        raise ValueError('Invalid host input')
    command = generate_ping_command(host)
    subprocess.run(command, shell=False, check=True)
    return {'status': 'completed'}
def is_safe_for_ping(input_str: str) -> bool:
    # Implement logic to validate the input
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return all(c in allowed_chars for c in input_str)