from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Constructing command safely using list for args parameter
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or '-' not in host:
        return {'error': 'Invalid host'}
    return safe_ping(host)