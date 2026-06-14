from fastapi import FastAPI
import subprocess

def sanitize_host(host: str) -> str:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)

def safe_ping(args: list[str]):
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed: {e.stderr}'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if '.' in sanitized_host and all(char.isalnum() or char == '.' for char in sanitized_host):
        args = ['ping', f'-c 1 {sanitized_host}']
        return safe_ping(args)
    else:
        return {'error': 'Invalid input'}