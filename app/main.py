from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation using check_output and avoiding shell=True
    try:
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "message": f'Ping to {host} successful'}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}