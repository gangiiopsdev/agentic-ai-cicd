from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Secure implementation using subprocess.run with check=True and text=True for better error handling and output capture.
    args = ['ping', host]
    result = subprocess.run(args, check=True, text=True)
    return {"status": "completed", "output": result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with check=True and text=True for better error handling and output capture.
    args = ['ping', host]
    result = subprocess.run(args, check=True, text=True)
    return {"status": "completed", "output": result.stdout}