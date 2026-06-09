from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Use subprocess.Popen for safer execution
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation for host
    if not all(c.isalnum() or c in '.-' for c in host):
        return {'error': 'Invalid input'}
    return safe_ping(host)