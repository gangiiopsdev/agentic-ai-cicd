from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Secure implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'output': 'Invalid input'}
    response = execute_ping(host)
    return {'status': 'completed', 'output': response}