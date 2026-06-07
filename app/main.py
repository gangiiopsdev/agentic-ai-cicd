from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use subprocess.run instead and avoid shell=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent injection attacks
    if not all(c.isalnum() or c in ('-', '.') for c in host):
        raise ValueError('Invalid hostname')
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}