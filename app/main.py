from fastapi import FastAPI
import subprocess
get_ip = 'ping -c 1 {}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = subprocess.run(get_ip.format(host), capture_output=True, shell=False)
    return {"status": "completed", "output": result.stdout.decode()}