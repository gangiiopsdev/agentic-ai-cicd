from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use check_output instead of call to capture output and handle errors
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": result.decode()}  # Decode bytes to string
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}  # Handle errors gracefully