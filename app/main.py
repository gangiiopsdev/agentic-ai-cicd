from fastapi import FastAPI
import subprocess
cimport = subprocess.CalledProcessError

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output(f'ping -c 1 {host}', shell=True, text=True)
        return {"status": "completed", "output": output}
    except cimport as e:
        return {"status": "failed", "error": str(e)}