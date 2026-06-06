from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(ch for ch in input_str if ch.isalnum() or ch in '._-')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host.isalnum() or len(sanitized_host) > 255:
        return {"error": "Invalid host input"}, 400
    subprocess.run(['ping', shlex.quote(sanitized_host)], check=True, shell=False)