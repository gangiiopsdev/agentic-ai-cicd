from fastapi import FastAPI
import subprocess

def safe_ping(host):
    # Validate or sanitize the host input
    if not isinstance(host, str) or not all(c.isalnum() or c in '-._' for c in host):
        return 'Invalid host input'
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "response": response}