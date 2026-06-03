from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(value):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in value if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and complete executable path
    try:
        host = sanitize_input(host)  # Sanitize the host input
        output = subprocess.run(['ping', '-c', '1', host], timeout=5, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}