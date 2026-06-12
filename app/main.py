from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        # Validate and sanitize host input
        if not all(c.isalnum() or c in '.-+' for c in host):
            raise ValueError('Invalid hostname')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize host input
        if not all(c.isalnum() or c in '.-+' for c in host):
            raise ValueError('Invalid hostname')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}