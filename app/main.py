from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def secure_ping(command):
    result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = result.communicate()
    return output.decode(), error.decode() if error else None

def sanitize_input(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    return shlex.split(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        command = ['ping'] + sanitize_input(host)
        output, error = secure_ping(command)
        return {"status": "completed", "output": output, "error": error}
    except ValueError as e:
        return {"status": "error", "message": str(e)}