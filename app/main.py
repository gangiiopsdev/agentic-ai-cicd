from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        if not host or ' ' in host or '.' not in host:
            return {"error": "Invalid host"}
        command = shlex.split('ping {}'.format(host))
        subprocess.run(command, check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}