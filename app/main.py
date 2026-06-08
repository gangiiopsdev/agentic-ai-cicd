from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    # Safe implementation
    args = ['ping', host]
    for arg in args:
        if not isinstance(arg, str) or not arg.isalnum():
            raise ValueError('Invalid argument')
    subprocess.run(args, check=True)