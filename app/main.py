from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host name')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

def is_valid_host(host: str) -> bool:
    # Simple validation example
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(c in allowed_chars for c in host)

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': ping_safe(host)}