from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return {"status": "completed", "output": output.decode()}  # Return ping output if needed
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e.output)}