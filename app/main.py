from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Validate and sanitize the input
        if not host.isalnum():
            raise ValueError("Invalid hostname")
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {
            "status": "completed",
            "stdout": result.stdout.decode(),
            "stderr": result.stderr.decode()
        }
    except subprocess.CalledProcessError as e:
        return {
            "error": str(e),
            "stdout": e.stdout.decode() if hasattr(e, 'stdout') else '',
            "stderr": e.stderr.decode() if hasattr(e, 'stderr') else ''
        }

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)