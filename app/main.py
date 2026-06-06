from fastapi import FastAPI
import subprocess

global_app = FastAPI()

@global_app.get(")")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@global_app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and proper argument passing
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}