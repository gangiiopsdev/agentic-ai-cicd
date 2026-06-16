from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in '-_.' or c.isdigit())

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        subprocess.call(shlex.split(f'ping -c 1 {sanitized_host}'))
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}