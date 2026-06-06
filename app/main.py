from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isspace())

def run_subprocess(command: list, *args, **kwargs):
    try:
        output = subprocess.run(command, capture_output=True, text=True, check=True, *args, **kwargs)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return None

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', *sanitized_host.split()] if ' ' in sanitized_host else ['ping', sanitized_host]
    output = run_subprocess(command)
    return {"status": "completed", "output": output} if output else {"status": "failed", "error": "Ping failed or no output received"}