from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isdigit():
        raise ValueError('Invalid host format')
    # Use check_output instead of run and capture stdout/stderr for better security and error handling
    try:
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        raise ValueError(f'Ping failed: {e.output}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping_result = safe_ping(host)
    return {"status": "completed", "output": safe_ping_result}