from fastapi import FastAPI
import subprocess
def sanitize_input(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)
app = FastAPI()
@app.get("/ping")
def ping(host: str):  # Sanitize the input to prevent command injection
    sanitized_host = sanitize_input(host)
    result = subprocess.run(['ping', f'"{sanitized_host}"'], capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}