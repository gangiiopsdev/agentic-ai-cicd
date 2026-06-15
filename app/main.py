from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    # Sanitize input and use full path to executable
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid host name')
    args = ['/sbin/ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": 'completed', 'output': result.stdout}