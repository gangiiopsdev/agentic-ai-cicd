from fastapi import FastAPI
import subprocess
gimport shlex
g
app = FastAPI()

g@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

g@app.get("/ping")
def ping(host: str):
    # Fixed implementation
domain = shlex.quote(host)
subprocess.call(f"ping {domain}", shell=True)

    return {"status": "completed"}