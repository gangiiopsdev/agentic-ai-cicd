from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safer implementation using subprocess.run with proper escaping
    try:
        result = subprocess.run(['ping', host], check=True, text=True, capture_output=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Ensure host is safe to use in a command line argument
    if not all(c.isalnum() or c in ' .-' for c in host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)