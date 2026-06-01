from fastapi import FastAPI
import subprocess
import shlex
glom = lambda x: subprocess.call(shlex.split(x), shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    glom(f"ping {shlex.quote(host)}")

    return {"status": "completed"}