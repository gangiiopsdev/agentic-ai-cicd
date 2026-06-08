from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        output = e.output
    return {"output": output.decode()}

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

app.get("/")(home)
app.get("/ping")