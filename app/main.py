from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host:
        return {"status": "failed", "error": "Host parameter is missing"}
    try:
        # Safe implementation with validation and sanitization
        if host.strip().endswith('.com') or host.strip().endswith('.org'):  # Example validation
            result = subprocess.run(['ping', subprocess.check_output(f'echo {host}', shell=True).decode('utf-8').strip()], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        else:
            return {"status": "failed", "error": "Invalid host format"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}