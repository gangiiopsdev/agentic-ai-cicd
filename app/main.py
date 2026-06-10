from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/)")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run without shell=True
    args = ["ping", host]
    for arg in args:
        if not isinstance(arg, str) or (isinstance(arg, str) and '&&' in arg):
            raise ValueError("Invalid input")
    subprocess.call(args)
    return {"status": "completed"}