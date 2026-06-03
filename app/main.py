from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Sanitize input to prevent command injection
    if 'ping' in host or '\' in host:
        raise ValueError('Invalid host value')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'output': result.stdout}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)