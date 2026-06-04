from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return f'Error: {e}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input before using it in the subprocess call
    if not host or ' ' in host or ';' in host:
        return 'Invalid input'
    return safe_ping(host)