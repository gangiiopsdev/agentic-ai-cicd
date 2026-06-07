from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host or ' ' in host:
        raise ValueError('Invalid host input')
    args = ['ping'] + shlex.split(host)
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    output = safe_ping(host)
    return {"status": output}