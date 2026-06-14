from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    try:
        args = shlex.split(f'ping {host}')
        if not all(arg.isalnum() for arg in args[1:-1]):  # Validate arguments except the first and last
            return {"status": "failed", "error": "Invalid arguments"}
        subprocess.call(args)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}