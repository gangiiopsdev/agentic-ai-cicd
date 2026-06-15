from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = ''.join(char for char in host if char.isalnum() or char in '.-_')
    args = ['ping', safe_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'stdout': result.stdout, 'stderr': result.stderr}

@app.get("/ping")
def ping_route(host: str):
    if validate_input(host):
        return ping(host)
    else:
        return {'error': 'Invalid input'}

def validate_input(input_str: str) -> bool:
    # Robust validation logic
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return all(char in allowed_chars for char in input_str)