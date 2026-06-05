from fastapi import FastAPI
import subprocess
class SafePinger:
    @staticmethod
def safe_ping(host):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent shell injection
    if not host.isalnum():
        raise ValueError('Invalid characters in host name')
    return SafePinger.safe_ping(host)