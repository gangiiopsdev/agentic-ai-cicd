from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Validate and sanitize input
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(char in allowed_chars for char in host):
        return {"error": "Invalid input"}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": result.stdout}

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run without shell=True
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(char in allowed_chars for char in host):
        return {"error": "Invalid input"}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": result.stdout}