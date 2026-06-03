from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if all(char in allowed_chars for char in host) and len(host) <= 255:
        try:
            result = subprocess.run(["ping", host], capture_output=True, text=True, timeout=10)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.TimeoutExpired:
            return {'error': 'Ping request timed out'}
    else:
        return {'error': 'Invalid input'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)