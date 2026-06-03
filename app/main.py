from fastapi import FastAPI
import subprocess
import shlex


global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and check=True
    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), check=True, stdout=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}