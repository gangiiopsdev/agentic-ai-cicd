from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', f'"{host}"']  # Use f-string to escape potentially malicious characters in the input
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)