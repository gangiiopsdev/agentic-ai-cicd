from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote

app = FastAPI()

def run_command(cmd):
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return e.output

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    cmd = ['ping', cmd_quote(host)]
    output = run_command(cmd)
    return {"status": "completed", "output": output}