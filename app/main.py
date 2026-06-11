from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        command = shlex.split(f'ping -c 1 {sanitized_host}')
        output = subprocess.run(command, capture_output=True, text=True, timeout=5)
        return {"status": "completed", "output": output.stdout}
    except subprocess.TimeoutExpired:
        return {"status": "failed", "error": "Command timed out"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}