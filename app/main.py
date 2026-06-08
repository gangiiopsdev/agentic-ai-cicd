from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation using subprocess.run with shell=False and arg substitution
        subprocess.run(['ping', host], check=True, capture_output=True)
        return {"status": "completed", "stdout": subprocess.getoutput('ping ' + host)}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}