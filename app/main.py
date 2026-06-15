from fastapi import FastAPI
import subprocess
import shlex
def execute_ping(host: str):
    # Safe implementation
    args = ['ping', host]
    subprocess.run(args)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    execute_ping(shlex.quote(host))
    return {"status": "completed"}