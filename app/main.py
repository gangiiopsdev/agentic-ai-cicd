from fastapi import FastAPI
import subprocess
import shlex
def run_command(command):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    except subprocess.TimeoutExpired as e:
        return {"status": "timed out", "error": str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = host.strip()  # Sanitize input to prevent injection attacks
    command = shlex.split(f'ping {sanitized_host}')
    return run_command(command)