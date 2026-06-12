from fastapi import FastAPI
import subprocess
import shlex
global host
host = '127.0.0.1' # default value for demonstration purposes
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    command = ["ping", *shlex.split(host)]
    try:
        subprocess.run(command, check=True, text=True, capture_output=True)
        return {"status": "completed", "stdout": result.stdout, "stderr": result.stderr}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "stdout": e.stdout, "stderr": e.stderr}