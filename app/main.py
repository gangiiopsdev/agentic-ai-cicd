from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize the input
        if not host.isdigit() or int(host) < 0:
            raise ValueError("Invalid input")
        output = subprocess.check_output(shlex.split(f'ping -c 1 {host}'), stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    except ValueError as ve:
        return {"status": "failed", "error": str(ve)}