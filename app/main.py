from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    safe_host = shlex.quote(host)
    subprocess.call(['ping', safe_host])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_command(host: str):
    # Fixed implementation
    try:
        subprocess.run(['ping', host], check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}