from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Safe implementation using subprocess.run without shell=True
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=10)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if ' ' in host or '\' in host or ';' in host or '&' in host or '|' in host:
        return "Invalid input"
    return run_ping(host)