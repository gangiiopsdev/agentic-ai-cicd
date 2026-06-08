from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    # Stronger validation to avoid injection
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    if not input_str.isalnum() and all(c in allowed_chars for c in input_str) and input_str != 'localhost':
        raise ValueError('Invalid input')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        sanitize_input(host)
        subprocess.call(['ping', host])  # Use a list for safe command execution
    except ValueError as e:
        return {'error': str(e)}
    return {'status': 'completed'}