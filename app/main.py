from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize host input to prevent command injection
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized_host = ''.join(char for char in host if char in allowed_chars)
    try:
        result = subprocess.run(['ping', '-c 1', sanitized_host], check=True, capture_output=True, text=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate host input to prevent command injection
    if not all(char in allowed_chars for char in host):
        return {'error': 'Invalid characters in host input'}
    return safe_ping(host)