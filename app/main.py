from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Secure implementation
        safe_host = subprocess.quote(host)
        subprocess.call(['ping', safe_host])

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return SafePing.ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}