from fastapi import FastAPI
import subprocess

def execute_ping(host):
    # Validate the host input to prevent command injection
    if not all(c.isalnum() or c in '-.' for c in host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=False)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    return execute_ping(host)