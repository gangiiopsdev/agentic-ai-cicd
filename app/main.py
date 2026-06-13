from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    cmd = ['ping', *shlex.split(host)]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return result.stdout

global_result = ""
app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global global_result
    try:
        result = safe_ping(host)
        global_result = result
        return {"status": "completed", "output": result}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}