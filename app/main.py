from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with proper argument passing and input validation
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid hostname'}
    result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}