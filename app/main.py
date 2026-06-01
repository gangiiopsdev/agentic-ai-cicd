from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        command = shlex.split(f'ping {host}')
        # Validate or sanitize the host input
        if not is_valid_host(host):
            return {'error': 'Invalid host'}
        subprocess.call(command)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}
def is_valid_host(host: str) -> bool:
    # Add validation logic here
    return True