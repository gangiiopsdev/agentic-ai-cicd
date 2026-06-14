from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Use subprocess.run to avoid shell=True and ensure the host is properly sanitized
    try:
        result = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Use the safe_ping function to avoid shell=True
    if shlex.split(host) != [host]:  # Simple check to prevent command injection
        return {'status': 'error', 'message': 'Invalid input'}
    return {'status': 'completed', 'result': safe_ping(host)}