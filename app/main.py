from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Using subprocess.run for a safer approach
        subprocess.run(['ping', host], check=True, timeout=5)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error: {e}'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)