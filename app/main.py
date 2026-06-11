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
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        return {"error": "Ping failed", "output": e.output.decode()}
    return {"status": "completed", "output": output.decode()}