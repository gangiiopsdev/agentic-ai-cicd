from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host == 'localhost' or host == '127.0.0.1':
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
            return {"status": "completed", "output": output.decode()} 
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.output.decode()}
    else:
        return {"status": "failed", "error": "Invalid host"}