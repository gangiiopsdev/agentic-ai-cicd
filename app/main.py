from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(char for char in input_string if char.isalnum() or char in ('-', '.', '_'))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {"error": "Invalid input"}
    subprocess.call(f"ping {shlex.quote(sanitized_host)}", shell=True)
    return {"status": "completed"}