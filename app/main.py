from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Validate host input to ensure it only contains allowed characters
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    if not all(char in allowed_chars for char in host):
        raise ValueError("Invalid host")

    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}