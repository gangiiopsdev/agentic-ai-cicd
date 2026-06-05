from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e == '.' or e == '-').strip()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to avoid shell injection
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed"}