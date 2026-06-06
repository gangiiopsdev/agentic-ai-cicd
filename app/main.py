from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        # Validate the host input to ensure it's a valid hostname or IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {'error': 'Invalid host'}
        args = shlex.split(f'ping {host}')
        subprocess.call(args)
    except Exception as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)