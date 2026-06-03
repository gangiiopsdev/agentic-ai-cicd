from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    return SafePing.ping(host)