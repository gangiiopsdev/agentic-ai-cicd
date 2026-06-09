from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(ch for ch in input_string if ch.isalnum() or ch in ['.', '-', '_'])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_input(host)
    try:
        output = subprocess.check_output(['ping', shlex.quote(safe_host)], stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        output = e.output
    return {"status": "completed", "output": output.decode()}