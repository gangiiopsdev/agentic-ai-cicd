from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()
def sanitize_input(input_string):
    allowed_characters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(c for c in input_string if c in allowed_characters)
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(shlex.split(f'ping {sanitized_host}'), capture_output=True, text=True, check=True)
    return {"status": "completed"}