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
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "output": str(e.output)}
    return {"status": "completed", "output": output.decode()}