from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/home')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the hostname to ensure it does not contain any malicious characters or patterns
        if not host.isalnum() and not '.' in host:
            return {"status": "failed", "error": "Invalid hostname"}
        output = subprocess.check_output(shlex.split(f'ping {host}'), stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    except subprocess.TimeoutExpired as e:
        return {"status": "timeout", "message": str(e)}