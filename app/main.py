from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    # Add your sanitization logic here
    return ''.join(e for e in input_string if e.isalnum() or e in [".", "-"])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    subprocess.call(args)
    return {"status": "completed"}