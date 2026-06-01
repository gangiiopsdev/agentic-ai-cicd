from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(char for char in input_string if char in allowed_chars)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation using subprocess.Popen instead of subprocess.call
    process = subprocess.Popen(['ping', sanitized_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {"status": "completed", "output": output.decode(), "error": error.decode() if error else None}