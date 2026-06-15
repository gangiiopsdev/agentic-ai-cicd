from fastapi import FastAPI
import subprocess
cimport re

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9]{1,}$', host) or '..' in host:
        return {'status': 'error', 'message': 'Invalid host input'}
    result = subprocess.run(['ping', '--', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}