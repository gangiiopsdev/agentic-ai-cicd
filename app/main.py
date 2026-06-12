from fastapi import FastAPI
import subprocess
import shlex

g-import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        args = shlex.split(f'ping -c 1 {host}')  # Limit the number of pings to avoid abuse
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    else:
        return {"status": "completed"}