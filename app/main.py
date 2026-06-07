from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get('/home')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isdigit() or len(host) > 15:
        return {"error": "Invalid host"}
    try:
        result = subprocess.run(['ping', '-c', '4', shlex.quote(host)], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}