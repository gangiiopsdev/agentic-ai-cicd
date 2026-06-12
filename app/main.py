from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        output = subprocess.check_output(['ping', host], universal_newlines=True, timeout=10)
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}