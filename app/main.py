from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        safe_host = subprocess.list2cmdline([host])
        result = subprocess.call(['ping', '-c', '1', safe_host])
        return {'status': 'completed'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return SafePing.ping(host)