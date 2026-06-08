from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Secure implementation using check_output with shell=False and passing args separately
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}