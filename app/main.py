from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation and proper argument handling
    if not host or not host.isalnum():
        return {"status": "invalid host"}
    command = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {
            "status": "completed",
            "output": result.stdout.decode()
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "error",
            "message": str(e),
            "stdout": e.stdout.decode(),
            "stderr": e.stderr.decode()
        }