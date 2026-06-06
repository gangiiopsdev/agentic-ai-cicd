from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ' '.join(filter(lambda x: str(x).strip().isalnum() or str(x).strip() in ['-', '_', '.'], input_string.split()))

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(shlex.split(f"ping {sanitized_host}"))
    return {"status": "completed"}