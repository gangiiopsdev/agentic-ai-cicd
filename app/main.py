from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    safe_host = shlex.quote(host)
    return f'ping -c 1 {safe_host}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.run(shlex.split(safe_ping(host)), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}