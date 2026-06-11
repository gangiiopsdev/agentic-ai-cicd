from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in ['127.0.0.1', '::1']:  # Allow only localhost for demonstration
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}