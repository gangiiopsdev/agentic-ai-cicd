from fastapi import FastAPI
import subprocess
global host

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(_host: str):
    global host
    host = _host
    try:
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    return {"status": "completed"}