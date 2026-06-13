from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(char for char in input_string if char.isalnum() or char == '.' or char == '-')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation using subprocess.Popen
    subprocess.Popen(['ping', sanitized_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}