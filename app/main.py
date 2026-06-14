from fastapi import FastAPI
import subprocess
import shlex

def execute_ping(host: str):
    try:
        args = ['ping', host]
        result = subprocess.run(shlex.split(' '.join(args)), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Simple input validation to prevent command injection
        return {'status': 'failed', 'error': 'Invalid input'}
    return execute_ping(host)