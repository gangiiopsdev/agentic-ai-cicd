from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate host input to ensure it does not contain harmful characters or patterns
    if any(char in host for char in [';', '&', '|', '>', '<', '*', '?', '{', '}', '`']):
        raise ValueError('Invalid host name')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation using subprocess.run with input validation
        result = subprocess.run(['ping', safe_ping(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}