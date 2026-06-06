from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    # Basic input sanitization (example)
    return ''.join(e for e in input_string if e.isalnum() or e in ['-', '.', '_', ' ', ',', ':', ';'])

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', shlex.quote(sanitized_host)]
    subprocess.call(command, shell=False)
    return {"status": "completed"}