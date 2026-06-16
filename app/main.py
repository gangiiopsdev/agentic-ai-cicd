from fastapi import FastAPI
import subprocess
import shlex
from html import escape

app = FastAPI()

def sanitize_input(input_string):
    return escape(input_string)

def run_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host != host:
        raise ValueError("Invalid input")
    command_parts = shlex.split(f'ping {sanitized_host}')
    output = run_safe_command(command_parts)
    return {"status": "completed", "output": output}