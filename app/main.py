from fastapi import FastAPI
import subprocess
global ping
ping = lambda host: subprocess.call(['ping', '-c', '4', host])
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    return {'status': ping(host)}