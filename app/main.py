from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_ping(host: str):
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        run_ping(shlex.quote(host))
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}