from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get"")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use shlex to safely handle the command and arguments
        output = subprocess.check_output(shlex.split(f'ping {host}'), stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}