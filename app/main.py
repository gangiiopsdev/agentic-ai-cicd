from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with shell=False and proper validation
    if not all(c.isalnum() or c in ['-', '.', '_', ','] for c in host):  # Basic input validation
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': safe_ping(host)}