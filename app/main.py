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
        # Secure implementation using subprocess.run and shlex.split
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, check=True)
        return {"status": "completed", "result": result.returncode}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}