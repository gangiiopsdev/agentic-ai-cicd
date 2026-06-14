from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate user input to prevent command injection
        allowed_hosts = ['example.com', 'test.com']  # Define a whitelist of allowed hosts
        if host not in allowed_hosts:
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}