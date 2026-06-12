from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation without shell=True
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except subprocess.TimeoutExpired:
        return 'Ping timed out'

@app.get("/ping")
def ping(host: str):
    # Using the safe implementation
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}