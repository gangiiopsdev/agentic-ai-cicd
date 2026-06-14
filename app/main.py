from fastapi import FastAPI
import subprocess
import shlex

global_vars = globals()
app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize the input to avoid injection attacks
        if not host.replace('.', '').isdigit() or '&&' in host or ';' in host or '|' in host:
            raise ValueError('Invalid host format')
        subprocess.run(shlex.split(f'ping -c 1 {host}'), check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}