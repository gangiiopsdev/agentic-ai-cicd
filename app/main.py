from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        return {'status': 'error', 'output': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}