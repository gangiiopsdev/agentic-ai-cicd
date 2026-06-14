from fastapi import FastAPI
import subprocess
import shlex

global shell_mode
shell_mode = False

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and proper argument handling
    try:
        result = subprocess.run(['ping', *shlex.split(host)], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": e.stderr}