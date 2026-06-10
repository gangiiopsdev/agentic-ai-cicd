from fastapi import FastAPI
import subprocess
g-import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        args = shlex.split(f'ping -c 4 {host}')  # Limit the number of pings to avoid denial of service
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    else:
        return {"status": "completed"}