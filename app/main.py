from fastapi import FastAPI
import subprocess
import shlex
g import shlex
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize the input more strictly
        if not host.isalnum() or '..' in host or ';' in host or '&' in host or '|' in host or '`' in host or '($)' in host:
            raise ValueError("Invalid host name")
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}