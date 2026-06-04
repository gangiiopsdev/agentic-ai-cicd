from fastapi import FastAPI
import subprocess
cimport subprocess as sp

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Secure implementation using subprocess.run with shell=False and split command into arguments
        sp.run(['ping', host], check=True, stdout=sp.PIPE, stderr=sp.PIPE)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}