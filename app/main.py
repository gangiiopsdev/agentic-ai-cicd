from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    if not host.isalnum() or 'ping' in host:
        return {'error': 'Invalid input'}
    args = ['ping', host.replace(';', '')]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}