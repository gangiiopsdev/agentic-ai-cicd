from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.startswith('localhost') or host.startswith('127.0.0.1'):
        return subprocess.run(['ping', host], capture_output=True, text=True)
    else:
        raise ValueError('Unsafe command detected')

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = safe_ping(host)
    return {
        "status": "completed",
        "output": result.stdout,
        "stderr": result.stderr
    }