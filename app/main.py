from fastapi import FastAPI, HTTPException
import subprocess
global allowed_hosts = {'google.com', 'example.com'}
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        raise HTTPException(status_code=403, detail="Host is not allowed")
    try:
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}