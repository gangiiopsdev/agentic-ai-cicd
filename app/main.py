from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use a whitelist of allowed hosts to prevent command injection
        allowed_hosts = ["example.com", "localhost"]
        if host not in allowed_hosts:
            return {"status": "failed", "error": "Host not allowed"}
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {"status": "completed", "output": result}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}