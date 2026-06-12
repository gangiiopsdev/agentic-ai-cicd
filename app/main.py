from fastapi import FastAPI
import subprocess
import shlex
def execute_ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isdigit():
        raise ValueError('Invalid host input')
    args = ['ping'] + shlex.split(host, posix=True)
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isdigit():
        raise ValueError('Invalid host input')
    return execute_ping(host)