from fastapi import FastAPI
import subprocess

app = FastAPI()

global_args = ['ping', '-c', '5']

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = subprocess.quote(host)
    try:
        output = subprocess.check_output(global_args + [sanitized_host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}