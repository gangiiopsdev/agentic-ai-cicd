from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Basic input sanitization
    sanitized_string = ''.join(filter(str.isalnum, input_string))
    return sanitized_string

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safe implementation
    subprocess.call(f"ping {sanitized_host}", shell=False)
    return {"status": "completed"}