from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Sanitize the host input to prevent shell injection
        if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
            raise ValueError('Invalid host name')
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)