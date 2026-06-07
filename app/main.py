from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Use shlex to safely handle the command arguments
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent code injection
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    sanitized_host = ''.join(char for char in host if char in allowed_chars)
    return safe_ping(sanitized_host)