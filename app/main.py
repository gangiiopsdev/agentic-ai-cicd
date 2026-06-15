from fastapi import FastAPI
import subprocess
import shlex
from html import escape

app = FastAPI()

def sanitize_input(input_string):
    return escape(input_string)

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