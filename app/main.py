from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get="/ping")
def ping(host: str):
    if 'ping' not in host:
        return {'error': 'Invalid input'}
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}