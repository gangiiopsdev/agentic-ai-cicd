from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    # Secure implementation using subprocess.run for better control and error handling
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr.strip()}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return run_ping(host)