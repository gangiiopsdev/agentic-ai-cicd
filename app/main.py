from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(value):
    # Add your sanitization logic here, e.g., whitelist or regex
    return value

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}