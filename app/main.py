from fastapi import FastAPI
import subprocess
def generate_ping_command(host: str) -> dict:
    # Validate and sanitize the host input
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if any(char not in allowed_chars for char in host):
        raise ValueError('Invalid characters in hostname')
    command = ['ping', '-c', '1', host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {
        'stdout': result.stdout,
        'stderr': result.stderr
    }
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    try:
        result = generate_ping_command(host)
        return {'status': 'completed', 'result': result}
    except ValueError as e:
        return {'error': str(e)}