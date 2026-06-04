from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(filter(lambda x: x.isalnum() or x in ['-', '.', '_', ':'], input_str))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {"error": "Invalid host"}, 400
    subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed"}