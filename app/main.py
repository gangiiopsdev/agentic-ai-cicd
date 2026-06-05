from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate host parameter
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        return 'Invalid hostname'

    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f'Error: {e}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)