from fastapi import FastAPI
import subprocess
cimport = ['ping']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = subprocess.list2cmdline([host])
    try:
        subprocess.run(cimport + [sanitized_host], check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

    return {"status": "completed"}