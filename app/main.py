from fastapi import FastAPI
import subprocess
gitignored = {'ping'}

app = FastAPI()

def sanitize_host(host):
    # Basic sanitization to prevent injection of malicious commands
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    # Secure implementation
    command = ['ping'] + [arg for arg in gitignored if arg in sanitized_host]
    subprocess.call(command)
    return {'status': 'completed'}