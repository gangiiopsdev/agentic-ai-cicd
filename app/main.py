from fastapi import FastAPI
import subprocess
import shlex
good_hosts = {'google.com', 'example.com'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in good_hosts:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"error": "Invalid host"}