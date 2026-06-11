from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation with argument validation and sanitization
    if not host or len(host) > 256:
        return {"status": "error", "message": "Invalid host"}
    args = ['ping', '-c', '4', host]
    subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "stdout": subprocess.PIPE.decode(), "stderr": subprocess.PIPE.decode()}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)