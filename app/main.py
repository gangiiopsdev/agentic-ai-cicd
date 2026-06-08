from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command):
    return subprocess.run(command, check=True, text=True, capture_output=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = run_command(["ping", host])
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": e.stderr}