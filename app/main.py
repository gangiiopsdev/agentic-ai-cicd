from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate the input to prevent shell injection
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._:@')
    if any(c not in allowed_chars for c in host):
        raise ValueError("Invalid characters in host")
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}