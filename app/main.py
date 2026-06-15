from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(user_input):
    return ''.join(c for c in user_input if c.isalnum() or c in ('-', '.', '_'))

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    result = subprocess.run(shlex.split(f'ping {sanitized_host}'), capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}