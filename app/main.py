from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Add input sanitization logic here
    return input_string.strip()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    # Use subprocess.run instead of subprocess.call
    result = subprocess.run(["ping", host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}