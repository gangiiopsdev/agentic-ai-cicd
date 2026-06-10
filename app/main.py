from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        if host.isnumeric() or '.' in host:
            result = subprocess.call(['ping', '-c', '1', host])
            return {'status': 'completed'}
        else:
            raise ValueError('Invalid input')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return SafePing.ping(host)