from fastapi import FastAPI
import subprocess
global _ping_process

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global _ping_process
    if _ping_process is not None and _ping_process.poll() is None:
        _ping_process.terminate()
        _ping_process.wait()
    _ping_process = subprocess.Popen(f'ping {host}', shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}