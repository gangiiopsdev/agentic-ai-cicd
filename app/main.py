from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ('-', '.', '_', ':'))

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host != host:
        raise ValueError("Invalid input")
    subprocess.call(shlex.split(f'ping {sanitized_host}'))
    return {"status": "completed"}