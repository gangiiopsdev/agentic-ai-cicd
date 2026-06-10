from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    args = ['ping', *shlex.split(host)]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed", "result": "Ping successful"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}