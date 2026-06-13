from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    # Sanitize input to prevent shell injection
    return ''.join(e for e in user_input if e.isalnum() or e.isspace())

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    # Use subprocess.run instead of subprocess.call and avoid shell=True
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=False)
    return {"status": "completed", "output": result.stdout}