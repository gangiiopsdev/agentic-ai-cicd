from fastapi import FastAPI
import subprocess
get_ip = lambda ip: subprocess.call(['ping', '-c', '1', ip], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    get_ip(host)
    return {"status": "completed"}