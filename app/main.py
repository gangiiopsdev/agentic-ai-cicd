from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isdigit() or len(host) != 1:
        return {'status': 'error', 'message': 'Invalid host input'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}