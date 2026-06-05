from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    # Simple sanitization example, replace with appropriate logic
    return ''.join(e for e in input_str if e.isalnum() or e.isspace())

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}