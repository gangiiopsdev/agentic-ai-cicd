from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    args = ['ping', host]
    try:
        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        return {"status": "completed", "output": output.decode()}\n    except subprocess.CalledProcessError as e:\n        return {"status": "failed", "error": e.output.decode()}