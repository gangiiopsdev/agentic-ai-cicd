from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255:
        return {'error': 'Invalid input'}
    return safe_ping(host)