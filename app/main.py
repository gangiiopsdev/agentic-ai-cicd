from fastapi import FastAPI
import subprocess
import shlex
def safe_subprocess(cmd):
    return subprocess.run(shlex.split(cmd), capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host input to prevent command injection
        if not host.isalnum() or '@' in host:
            raise ValueError("Invalid host input")
        result = safe_subprocess(f'ping -c 4 {host}')
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}