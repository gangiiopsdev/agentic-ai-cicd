from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        response = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return response.stdout
    except subprocess.TimeoutExpired as e:
        return f'Ping timed out: {e}'

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': safe_ping(host)}