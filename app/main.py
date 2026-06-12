from fastapi import FastAPI
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        return {'status': 'error', 'message': 'Invalid host'}
    # Secure implementation using subprocess.run without shell=True
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}