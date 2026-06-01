from fastapi import FastAPI
import subprocess
gl = 'ping' # Sanitize inputs before using them in subprocess commands

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isnumeric(): # Basic input validation
        subprocess.call([gl, host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid host parameter"}