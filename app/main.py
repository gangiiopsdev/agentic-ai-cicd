from fastapi import FastAPI
import subprocess
globally_safe_hosts = {'127.0.0.1', 'localhost'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in globally_safe_hosts:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'output': result.stdout, 'stderr': result.stderr}
    else:
        return {"error": "Host not allowed"}
    return {"status": "completed"}