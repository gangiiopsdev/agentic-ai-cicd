from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using check_output to capture output and prevent shell injection
    try:
        args = ['ping', host]
        result = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": result.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": e.output.decode()}