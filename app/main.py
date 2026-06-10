from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        # Secure implementation using subprocess.run
        subprocess.call(['ping', host])

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return SafeSubprocess.ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}