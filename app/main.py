from fastapi import FastAPI
import subprocess
import shlex

global allow_ping
allow_ping = False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not allow_ping:
        raise Exception("Ping functionality is disabled for security reasons.")
    try:
        args = shlex.split('ping ' + host)
        subprocess.call(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "result": "Success"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}