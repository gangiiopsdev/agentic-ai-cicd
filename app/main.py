from fastapi import FastAPI
import subprocess
gitignore = [
    'allowed_chars',
    'sanitized_host'
]

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_!@#$%^&*()+=[]{}|;:,.<>?/`\t'
    sanitized_host = ''.join(char for char in host if char in allowed_chars)

    # Use subprocess.run instead of subprocess.call
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}