from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get="/)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host.strip() == 'localhost':
        subprocess.call(shlex.split('ping ' + shlex.quote(host)))
    else:
        return {"status": "Invalid host"}

    return {"status": "completed"}