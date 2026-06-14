from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in '.-')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(f"ping {sanitized_host}", shell=True)
    return {"status": "completed"}