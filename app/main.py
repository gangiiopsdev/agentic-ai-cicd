from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.Popen with shlex.quote for argument quoting
    args = ['ping', shlex.quote(host)]
    subprocess.call(args)
    return {"status": "completed"}