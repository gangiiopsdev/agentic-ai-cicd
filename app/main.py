from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using Popen and shlex
    args = shlex.split('ping ' + host)
    process = Popen(args, stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    return {"status": "completed", "output": output.decode(), "error": error.decode() if error else None}