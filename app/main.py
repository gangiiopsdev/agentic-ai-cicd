from fastapi import FastAPI
import subprocess
def is_safe_host(host: str) -> bool:
    return '-' not in host and '/' not in host and ' ' not in host
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        if not is_safe_host(host):
            raise ValueError('Unsafe input detected')
        subprocess.call(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafeSubprocess.ping(host)
    return {"status": "completed"}