from fastapi import FastAPI
import subprocess
import shlex
import re

cmd_pattern = re.compile(r'^[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}$')

app = FastAPI()

def safe_ping(host: str):
    if not cmd_pattern.match(host):
        raise ValueError('Invalid host format')
    cmd = ['ping'] + shlex.split(host)
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "output": result}
    except ValueError as e:
        return {"error": str(e)}