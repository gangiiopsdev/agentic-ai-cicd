from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isdigit())

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(f"ping {sanitized_host}", shell=False)
    return {"status": "completed"}