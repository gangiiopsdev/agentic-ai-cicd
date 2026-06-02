from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation using subprocess.Popen and shlex
        args = shlex.split(f"ping {host}")
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return {"status": "completed", "output": output.decode(), "error": error.decode() if error else None}
    except Exception as e:
        return {"status": "failed", "error": str(e)}