from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and shlex to safely handle the command arguments
    try:
        args = ['ping', '-c', '1'] + shlex.split(host)
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}

    except subprocess.TimeoutExpired as e:
        return {"status": "timed out"}