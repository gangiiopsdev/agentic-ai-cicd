from fastapi import FastAPI
import subprocess
c
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        output = e.output
    return {"status": "completed", "output": output.decode()}