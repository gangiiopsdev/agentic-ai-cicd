from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call and avoid shell=True for security reasons.
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)