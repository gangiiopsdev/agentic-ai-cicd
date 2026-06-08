from fastapi import FastAPI
import subprocess
import shlex

def execute_ping(host: str):
    try:
        safe_host = shlex.quote(host)
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    if not host.strip().isdigit() or len(host) > 15:
        return {'status': 'error', 'output': 'Invalid host'}
    return execute_ping(host)