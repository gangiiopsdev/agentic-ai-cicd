from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Validate and sanitize input
        host = subprocess.check_output(['id', host], stderr=subprocess.STDOUT).decode('utf-8').strip()
        if 'uid=0(root)' in host or 'gid=0(root)' in host:
            raise ValueError('Unauthorized user')
    except subprocess.CalledProcessError as e:
        raise Exception(f'Command failed: {e.output.decode()}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}