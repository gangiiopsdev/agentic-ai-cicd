from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it's a safe command
    if not host.isalnum() or '&&' in host or ';' in host:
        return {'status': 'error', 'message': 'Invalid input'}

    # Secure implementation using subprocess.run with shell=False and fully qualified executable path
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    if result.returncode != 0:
        return {'status': 'error', 'message': 'Ping failed'}
    return {'status': 'completed', 'output': result.stdout}