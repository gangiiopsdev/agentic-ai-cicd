from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Ensure host input is safe
    if 'ping' in host or '&' in host:
        raise ValueError('Unsafe input detected')
    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "output": response}