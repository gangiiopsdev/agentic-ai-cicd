from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Add your input sanitization logic here
    return input_string.strip()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}