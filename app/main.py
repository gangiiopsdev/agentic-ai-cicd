from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and args tuple
    try:
        subprocess.run(shlex.split('ping ' + host), capture_output=True, text=True, check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}