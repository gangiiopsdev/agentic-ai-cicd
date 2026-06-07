from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize input to prevent command injection
        allowed_hosts = ['example.com']  # Define a list of allowed hosts
        if host in allowed_hosts:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'failed', 'error': 'Host not allowed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}