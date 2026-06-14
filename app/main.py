from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        if not host.isalnum() or len(host) > 255:
            raise ValueError("Invalid host name")
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e.output)}