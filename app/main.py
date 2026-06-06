from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def safe_run(command: str, *args, **kwargs):
        args = shlex.split(command)
        result = subprocess.run(args, capture_output=True, text=True, check=False, *args, **kwargs)
        return result

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if not host.isalnum() or '&&' in host or ';' in host:
        return {"status": "failed", "error": "Invalid host value"}
    try:
        result = SafeSubprocess.safe_run(f'ping {host}', capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}