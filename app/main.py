from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

gitignore = [
    'allowed_chars',
    'sanitized_host'
]

@app.get("/ping")
def ping(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_!@#$%^&*()+=[]{}|;:,.<>?/`\t'
    sanitized_host = ''.join(char for char in host if char in allowed_chars)

    # Use subprocess.run instead of subprocess.call and shlex.quote to safely handle command arguments
    result = subprocess.run(shlex.split(f'ping {shlex.quote(sanitized_host)}'), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}