from fastapi import FastAPI
import subprocess

def safe_execute_ping(host: str):
    # Validate and sanitize host input
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    if not all(c in allowed_chars for c in host):
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()
@app.get="/ping")
def ping(host: str):
    output = safe_execute_ping(host)
    return {'status': 'completed', 'output': output}