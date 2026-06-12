from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Secure implementation using subprocess.Popen without shell=True
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return SafePing.ping(host)