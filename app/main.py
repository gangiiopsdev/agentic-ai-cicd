from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in '-._')

def ping(host: str):
    sanitized_host = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": sanitized_host.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": sanitized_host.stdout}