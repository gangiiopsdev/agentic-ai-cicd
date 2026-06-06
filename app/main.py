from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Secure implementation using subprocess.run with sanitized input
    try:
        cmd = ['ping', shlex.quote(host)]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)